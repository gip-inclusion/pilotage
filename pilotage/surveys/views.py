import enum

from django.db.models import TextChoices
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from pilotage.surveys.models import ESATAnswer, Survey, SurveyKind
from pilotage.surveys.utils import get_previous_and_next_step, get_step_form_class, get_step_informations


class CommonStep(enum.StrEnum):
    INTRODUCTION = "introduction"
    CONCLUSION = "conclusion"


class ESATStep(TextChoices):
    INTRODUCTION = CommonStep.INTRODUCTION, "introduction"
    ORGANIZATION = "organization", "l'établissement"
    WORKERS_SUPPORTED = "workers-supported", "les travailleur.euse.s accompagné.es"
    WORKERS_ENTRY = "workers-new", "les travailleurs admis dans l'année"
    ESTABLISHMENT_DISCOVERY = "establishment-discovery", "découverte de l'ESAT"
    ORDINARY_WORKING_ENVIRONMENT = "ordinary-working-environment", "volonté d'aller vers le milieu ordinaire"
    ORDINARY_WORKING_ENVIRONMENT_AND_CUSTOMERS_INVOLVEMENT = (
        "ordinary-working-environment-and-customers-involvement",
        "contact avec le milieu ordinaire et la clientèle",
    )
    WORKERS_LEFT = "workers-left", "les sorties"
    WORKERS_RIGHT_TO_RETURN = (
        "workers-right-to-return",
        "travailleurs et travailleuses ayant exercé leur droit au retour "
        "après avoir occupé un emploi en milieu ordinaire de travail",
    )
    SUPPORT_HOURS = "support-hours", "heures de soutien"
    FORMATIONS = "formations", "formations"
    SKILLS = "skills", "reconnaissance des compétences"
    DUODAYS = "duodays", "Duodays"
    SKILLS_NOTEBOOK = "skills-notebook", "carnet parcours et compétences"
    RETIREMENT = "retirement", "préparation à la retraite"
    LANGUAGE_ACCESSIBILITY = "language-accessibility", "adaptation du langage écrit et oral"
    WORKING_CONDITIONS = "working-conditions", "pouvoir d'agir sur les conditions de travail"
    PROFIT_SHARING = "profit-sharing", "rémunération et prime d'intéressement"
    INSURANCE_POLICY = "insurance-policy", "régime de prévoyance"
    MOBILITY_PROGRAM = "mobility-program", "aide à la mobilité"
    VOUCHERS = "vouchers", "chèques vacances et chèques cadeaux"
    SUNDAY_WORK = "sunday-work", "travail le dimanche"
    PARTNERSHIP_AGREEMENTS = "partnership-agreements", "conventions de partenariats"
    STAFF = "staff", "conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle"
    COMMERCIAL_OPERATION = "commercial-operation", "section d'Exploitation Commerciale"
    SOCIAL_ACTIVITY_BUDGET = "social-activity-budget", "budget de fonctionnement ou budget social"
    INVESTMENTS = "investments", "investissements"
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
            "steps_info": get_step_informations(steps_class, answer, exclude=CommonStep),
            "next_step_url": next_step_url,
            "previous_step_url": previous_step_url,
            "current_step": step,
            "next_step": next_step,
            **extra_context,
        },
    )
