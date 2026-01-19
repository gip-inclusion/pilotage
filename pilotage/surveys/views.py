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
    WORKERS_SUPPORTED = "workers-supported", "les travailleurs et travailleuses accompagné.e.s"
    WORKERS_ENTRY = "workers-new", "les travailleurs et travailleuses admis.e.s dans l’année"
    ESTABLISHMENT_DISCOVERY = "establishment-discovery", "découverte de l'ESAT"
    ORDINARY_WORKING_ENVIRONMENT = "ordinary-working-environment", "volonté d'aller vers le milieu ordinaire"
    ORDINARY_WORKING_ENVIRONMENT_AND_CUSTOMERS_INVOLVEMENT = (
        "ordinary-working-environment-and-customers-involvement",
        "contact avec le milieu ordinaire de travail et la clientèle",
    )
    WORKERS_LEFT = "workers-left", "les sorties"
    WORKERS_RIGHT_TO_RETURN = (
        "workers-right-to-return",
        "exercice du droit au retour après avoir occupé un emploi en milieu ordinaire de travail",
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


LABELS_INFORMATIONS = {
    ESATAnswer: {
        "nb_employee_worked": (
            "Inclus : CDI, CDD du 01/01 au 31/12 et salariés transversaux (comptable, qualité...).<br>"
            "ETP : C'est la force de travail réelle. Un salarié à temps plein présent toute l'année vaut 1 ETP. Un salarié à 50% vaut 0,5 ETP"  # noqa: E501
        ),
        "nb_worker_acc": (
            "Indiquez ici le nombre total de travailleurs (personnes physiques) ayant été sous contrat de soutien et d'aide par le travail (y compris les périodes d'essai et les mises à disposition) entre le 01/01 et le 31/12.<br>"  # noqa: E501
            "Si un travailleur est parti en cours d'année, il doit être comptabilisé.<br>"
            "Les stagiaires (MISP, PMSMP) ne sont pas comptabilisées ici."
        ),
        "mean_worker_age": (
            "Même périmètre que la question précédente donc hors stagiaires.<br>"
            "Calcul à faire sur les effectifs présents au 31/12/N-1"
        ),
        "mean_seniority": (
            "Même périmètre que la question précédente donc hors stagiaires.<br>"
            "Calcul à faire sur les effectifs présents au 31/12/N-1"
        ),
        "nb_worker_previous_mot": "Nous avons conscience que cette donnée peut-être difficile à obtenir. Dans ce cas, vous êtes invité à ne rien remplir et à préciser la situation dans la rubrique « Commentaires » disponible en fin de questionnaire.",  # noqa: E501
        "nb_worker_new": "Nous avons conscience que cette donnée peut-être difficile à obtenir. Dans ce cas, vous êtes invité à ne rien remplir et à préciser la situation dans la rubrique « Commentaires » disponible en fin de questionnaire.",  # noqa: E501
        "nb_worker_temporary": (
            "Les travailleurs absents pour maladie, congés, emploi à temps partiel, vacance de poste, ...<br>"
            "Cette disposition vous permet de maintenir ainsi votre capacité d’activité en bénéficiant via l’ASP de l’annualisation de l’aide au poste."  # noqa: E501
        ),
        "nb_worker_willing_mot": (
            "Formalisé à l'écrit dans leur projet personnalisé.<br>"
            "Volonté d'aller, à terme, vers un contrat de droit commun.<br>"
            "Stages exclus. Calcul toujours en file active donc un travail parti au cours de l'année doit être comptabilisé."  # noqa: E501
        ),
        "nb_worker_ft_job_seekers": "Calcul toujours en file active donc un travail parti au cours de l'année doit être comptabilisé",  # noqa: E501
        "prescription_delegate": "Sur année n-1",
        "pmsmp_refused": "Sur année n-1",
        "nb_worker_service": "Inclus : espaces verts, clôture, ...",
        "nb_worker_with_public": (
            "Inclus : blanchisserie, restaurant, cafétérie, recyclerie, ...<br>"
            "Comptabiliser les travailleurs qui sont sur des postes où le contact avec la clientèle est clé (ne pas comptabiliser les travailleurs qui ont des contacts occasionnels - exemple ceux qui sont à la blanchisserie sans être à l'accueil de la blanchisserie)"  # noqa: E501
        ),
        "pct_activity_outside": (
            "Raisonner en nombre d'ateliers.<br>"
            "Le nombre d'ateliers qui s'exercent hors les murs sur le nombre total d'ateliers proposés par l'ESAT.<br>"
            "Ne pas tenir compte du nombre de personne, d'heures ou du chiffre d'affaire généré par chaque atelier."
        ),
        "nb_worker_cumul_esat_ea": ("Ici, il ne faut pas comptabiliser par contrat mais par travailleur.<br>"),
        "nb_worker_cumul_esat_mot": ("Ici, il ne faut pas comptabiliser par contrat mais par travailleur.<br>"),
        "nb_worker_left": "Tous les départs (validés ou non pas la MDPH)",
        "nb_worker_left_ea": "Calcul en nombre de travailleurs file active.",
        "nb_worker_left_private": "Calcul en nombre de travailleurs file active.",
        "nb_worker_left_public": "Calcul en nombre de travailleurs file active.",
        "nb_worker_left_asso": "Calcul en nombre de travailleurs file active.",
        "nb_worker_left_other_reason": (
            "Total des travailleurs sortis - tous ceux sortis vers une entreprise adaptée ou le milieu ordinaire.<br>"
            "Calcul en nombre de travailleurs file active."
        ),
        "nb_worker_cdi": "Calcul en nombre de travailleurs file active.",
        "nb_worker_cdd": "Calcul en nombre de travailleurs file active.",
        "nb_worker_interim": "Calcul en nombre de travailleurs file active.",
        "nb_worker_prof": "Calcul en nombre de travailleurs file active.",
        "nb_worker_apprentice": "Calcul en nombre de travailleurs file active.",
        "nb_worker_esrp": "Calcul en nombre de travailleurs file active.",
        "nb_worker_reinteg": "Travailleurs et travailleuses ont réintégré l'ESAT après avoir occupé un emploi en milieu ordinaire de travail (entreprise classique ou adaptée ou tout autre organisme public ou privé)",  # noqa: E501
        "nb_worker_reinteg_other": (
            "Travailleurs et travailleuses ont réintégré un autre ESAT après avoir occupé un emploi en milieu ordinaire de travail ? (entreprise classique ou adaptée ou tout autre organisme public ou privé).<br>"  # noqa: E501
            "Comptabiliser tous les retours même si pas de convention de retour avec ESAT"
        ),
        "pct_opco": "Reportez-vous à votre bordereau de cotisation annuelle.",
        "nb_worker_cpf_unused": "Nous avons conscience que cette donnée peut-être difficile à obtenir. Dans ce cas, vous êtes invité à ne rien remplir et à préciser la situation dans la rubrique « Commentaires » disponible en fin de questionnaire.",  # noqa: E501
        "nb_worker_intern_formation": "Sont exclues les formations animées par des organismes externes, même si celles-ci ont lieu dans les murs de l’ESAT. Sont aussi exclus les apprentissages délivrés par les moniteurs durant la production quotidienne.",  # noqa: E501
        "nb_worker_autodetermination": "Les actions de sensibilisation à l’autodétermination doivent s’entendre comme des actions de formation ( prévu par les conventions OPCO Santé et OPCA ANFH).",  # noqa: E501
        "nb_worker_rae_rsfp": "Dont la RAE ou RSFP a été validée au cours de l'année",
        "nb_worker_vae": "Dont la VAE a été validée au cours de l'année",
        "documents_falclist": "Possible de répondre OUI si le document n'a été traduit que partiellement",
        "nb_worker_mobility_inclusion_card": "Nous avons conscience que cette donnée peut-être difficile à obtenir. Dans ce cas, vous êtes invité à ne rien remplir et à préciser la situation dans la rubrique « Commentaires » disponible en fin de questionnaire.",  # noqa: E501
        "annual_ca": "Reportez vous au guide d’aide au remplissage pour des indications précises",
        "annual_ca_production": "Reportez vous au guide d’aide au remplissage pour des indications précises",
        "annual_ca_service": "Reportez vous au guide d’aide au remplissage pour des indications précises",
        "annual_ca_mad": "Reportez vous au guide d’aide au remplissage pour des indications précises",
        "pct_ca_public": "Reportez vous au guide d’aide au remplissage pour des indications précises",
        "budget_commercial": "Solde final après inclusion des aides au poste - relatif uniquement à la partie commerciale",  # noqa: E501
        "budget_diversity": "Il s'agit ici des investissements ayant permis à l'ESAT de diversifier ses activités (nouveaux outils de production, etc.)",  # noqa: E501
    }
}


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
            "labels_information": LABELS_INFORMATIONS.get(answer_class),
            **extra_context,
        },
    )
