from django.db.models import TextChoices
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pilotage.surveys import forms as survey_forms
from pilotage.surveys.models import ESATAnswer, Survey, SurveyKind


class ESATStep(TextChoices):
    ORGANIZATION = "organization", "la structure"
    EMPLOYEE = "employee", "les employés"
    PMSMP = "pmsmp", "PMSMP"
    ACTIVITY_KIND = "activity-kind", "types d'activités"
    PARTIAL_WORK = "partial-work", "temps partiels et cumuls d'activités"
    EMPLOYEE_LEFT = "employee-left", "sorties"
    EMPLOYEE_RETURN = "employee-return", "droit au retour"
    MISC = "misc", "misc"
    RETIREMENT = "retirement", "préparation à la retraite"
    OPCO = "opco", "OPCO"
    SKILLS = "skills", "reconnaissance des compétences"
    CPF = "cpf", "CPF"
    AUTODETERMINATION = "autodetermination", "formation à l'autodétermination"
    DUODAY = "duoday", "Duoday"
    REPRESENTATIVE = "representative", "Délégués"
    BONUS = "bonus", "primes"
    HEALTH_ASSURANCE = "health-assurance", "complémentaire santé et prévoyance"
    MOBILITY = "mobility", "mobilité"
    VOUCHER = "voucher", "chèques vacances et cadeaux"
    CONVENTION = "convention", "conventions"
    COUNSELORS = "counselors", "conseillers en parcours d'insertion et chargé(e)s d'inclusion professionnelle"
    REVENUE = "revenue", "chiffre d'affaires"
    SALES_BUDGET = "sales-budget", "budget commercial"
    SOCIAL_ACTIVITY_BUDGET = "social-activity-budget", "budget principal de l'activité sociale"
    COMMENTS = "comments", "commentaires"


def start(request, *, survey_name):
    survey = get_object_or_404(Survey, name=survey_name)
    match survey.kind:
        case SurveyKind.ESAT:
            answer = ESATAnswer.objects.create(survey=survey)
            step_class = ESATStep
        case _:
            return HttpResponseNotFound()
    first_step = list(step_class)[0]
    return redirect(
        reverse(
            "surveys:tunnel",
            kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": first_step},
        )
    )


KNOWN_ACRONYM = {
    "PMSMP",
    "OPCO",
    "CPF",
}


def _get_step_form_class(answer_class, step):
    step_as_camel_case = (
        step.replace("-", " ").title().replace(" ", "") if step.upper() not in KNOWN_ACRONYM else step.upper()
    )
    return getattr(survey_forms, f"{answer_class.__name__}{step_as_camel_case}Form")


def _get_previous_and_next_step(steps, current_step):
    choices = list(steps)
    try:
        next_step = choices[choices.index(current_step) + 1]
    except IndexError:
        next_step = None
    try:
        previous_step = choices[choices.index(current_step) - 1]
    except IndexError:
        previous_step = None
    return previous_step, next_step


def tunnel(request, *, survey_name, answer_uid, step):
    survey = get_object_or_404(Survey, name=survey_name)
    match survey.kind:
        case SurveyKind.ESAT:
            answer_class, steps_class = ESATAnswer, ESATStep
        case _:
            return HttpResponseNotFound()

    answer = get_object_or_404(answer_class, uid=answer_uid)
    try:
        step = steps_class(step)
    except ValueError:
        return HttpResponseRedirect(
            reverse(
                "surveys:tunnel",
                kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": list(steps_class)[0]},
            )
        )
    previous_step, next_step = _get_previous_and_next_step(steps_class, step)
    form = _get_step_form_class(answer_class, step)(instance=answer, data=request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(
            reverse(
                "surveys:tunnel",
                kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": next_step},
            )
        )

    return render(
        request,
        "surveys/survey.html",
        context={
            "survey": survey,
            "answer": answer,
            "form": form,
            "title": step.label,
            "steps_class": steps_class,
            "previous_step_url": reverse(
                "surveys:tunnel", kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": previous_step}
            )
            if previous_step
            else None,
            "current_step": step,
            "next_step": next_step,
        },
    )
