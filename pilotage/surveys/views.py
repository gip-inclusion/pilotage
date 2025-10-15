import enum

from django.db.models import TextChoices
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pilotage.surveys.models import ESATAnswer, Survey, SurveyKind
from pilotage.surveys.utils import get_previous_and_next_step, get_step_form_class


class CommonStep(enum.StrEnum):
    INTRODUCTION = "introduction"
    CONCLUSION = "conclusion"


class ESATStep(TextChoices):
    INTRODUCTION = CommonStep.INTRODUCTION, "introduction"
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
    CONCLUSION = CommonStep.CONCLUSION, "conclusion"


def start(request, *, survey_name):
    survey = get_object_or_404(Survey.objects.open(), name=survey_name)  # Only open surveys can have new answers
    match survey.kind:
        case SurveyKind.ESAT:
            answer = ESATAnswer.objects.create(survey=survey)
            step_class = ESATStep
        case _:
            return HttpResponseNotFound()
    return redirect(
        reverse(
            "surveys:tunnel",
            kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": list(step_class)[0]},
        )
    )


def tunnel(request, *, survey_name, answer_uid, step):
    # Here we also include closed surveys so the respondent can see their answers
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
    previous_step, next_step = get_previous_and_next_step(steps_class, step)
    extra_context = {}
    if step in CommonStep:
        extra_context["content"] = getattr(survey, step)
    else:
        form = get_step_form_class(answer_class, step)(
            instance=answer, data=request.POST or None, editable=survey.is_open
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    "surveys:tunnel",
                    kwargs={
                        "survey_name": survey.name,
                        "answer_uid": answer.uid,
                        "step": previous_step if request.POST.get("goto") == "previous" else next_step,
                    },
                )
            )
        extra_context["form"] = form

    next_step_url = (
        reverse("surveys:tunnel", kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": next_step})
        if next_step
        else None
    )
    previous_step_url = (
        reverse("surveys:tunnel", kwargs={"survey_name": survey.name, "answer_uid": answer.uid, "step": previous_step})
        if previous_step
        else None
    )
    return render(
        request,
        "surveys/survey.html",
        context={
            "survey": survey,
            "answer": answer,
            "title": step.label,
            "steps_class": steps_class,
            "next_step_url": next_step_url,
            "previous_step_url": previous_step_url,
            "current_step": step,
            "next_step": next_step,
            **extra_context,
        },
    )
