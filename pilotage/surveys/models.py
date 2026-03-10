# FIXME: Remove the noqa once the verbose_name are confirmed
# ruff: noqa: E501

from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from django.utils.text import slugify

from pilotage.itoutils.departments import DEPARTMENTS
from pilotage.itoutils.validators import validate_finess, validate_siret
from pilotage.surveys.utils import get_field_text


def uuid7():
    try:
        from uuid import uuid7 as func
    except ImportError:
        from uuid_utils import uuid7 as func
    return str(func())


class SurveyKind(models.TextChoices):
    ESAT = "ESAT", "ESAT"


class SurveyQuerySet(models.QuerySet):
    def open(self):
        return self.filter(opening_period__contains=timezone.now())


class Survey(models.Model):
    kind = models.CharField(verbose_name="type", choices=SurveyKind.choices)
    vintage = models.CharField(verbose_name="millésime")
    name = models.SlugField(verbose_name="nom", unique=True, editable=False)
    opening_period = DateTimeRangeField(verbose_name="période d'ouverture")

    title = models.fields.CharField(null=True, blank=True, verbose_name="titre")
    introduction = models.fields.TextField(null=True, blank=True)
    conclusion = models.fields.TextField(null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    objects = SurveyQuerySet.as_manager()

    class Meta:
        verbose_name = "enquête"

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.name or slugify(f"{self.kind} {self.vintage}")
        super().save(**kwargs)

    @property
    def is_open(self):
        return timezone.now() in self.opening_period


class Answer(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid7, editable=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="answers", verbose_name="enquête")

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "réponse"

    def __str__(self):
        return str(self.uid)


DO_NOT_KNOW_CHOICE = ("DO_NOT_KNOW", "Je ne sais pas")
NO_CHOICE = ("NO", "Non")
OTHER_CHOICE = ("OTHER", "Autres")


class YesNoWIP(TextChoices):
    YES = "YES", "Oui"
    NO = NO_CHOICE
    WIP = ("WIP", "C'est en cours")


class BudgetFunding(TextChoices):
    BPAS = "BPAS", "Par votre budget de fonctionnement (BPAS)"
    BAPC = "BAPC", "Par votre budget annexe de production et de commercialisation (BAPC)"
    OTHER = OTHER_CHOICE


class BudgetState(TextChoices):
    SURPLUS = "SURPLUS", "excédentaire"
    BALANCE = "BALANCE", "à l'équilibre"
    DEFICIT = "DEFICIT", "déficitaire"


class BudgetRange(TextChoices):
    LESS_THAN_100K = "LESS_THAN_100K", "Moins de 100 k€"
    RANGE_100K_500K = "RANGE_100K_500K", "100 k€ à 500k€"
    MORE_THAN_500K = "MORE_THAN_500K", "Plus de 500k€"


class ESATLegalStatus(TextChoices):
    PUBLIC = "PUBLIC", "Public"
    NON_PROFIT = "NON_PROFIT", "Privé sans but lucratif"


class DocumentFALCList(TextChoices):
    CONTRACT = "CONTRACT", "Oui : contrat d'accompagnement par le travail"
    BOOKLET = "BOOKLET", "Oui : livret d'accueil"
    REGULATION = "REGULATION", "Oui : règlement de fonctionnement"
    NO = NO_CHOICE


class SupportHoursRange(TextChoices):
    LESS_THAN_50 = "LESS_THAN_50", "Moins de 50 heures"
    RANGE_100_150 = "RANGE_100_150", "Entre 100 et 150 heures"
    RANGE_150_200 = "RANGE_150_200", "Entre 150 et 200 heures"
    RANGE_200_250 = "RANGE_200_250", "Entre 200 et 250 heures"
    MORE_THAN_250 = "MORE_THAN_250", "Plus de 250 heures"
    UNKNOWN = "UNKNOWN", "Inconnu, non quantifiable"


class SupportThemes(TextChoices):
    WORKSHOP_JOB_SEARCH = "WORKSHOP_JOB_SEARCH", "Atelier d'accompagnement à la recherche d'emploi"
    WORKSHOP_WELLBEING = "WORKSHOP_WELLBEING", "Atelier de prévention santé / bien-être au travail"
    PROFESSIONAL_SUPPORT = "PROFESSIONAL_SUPPORT", "Activité de soutien au parcours professionnel"
    CPF_OPENED = "CPF_OPENED", "Ouverture du Compte Professionnel de Formation"
    COMPANY_TOUR = "COMPANY_TOUR", "Visites dans les entreprises"
    PREMISES_TOUR = "PREMISES_TOUR", "Visites des locaux de l’ESAT par les entreprises"
    OTHER = OTHER_CHOICE


class SkillsValidationType(TextChoices):
    RAE = "RAE", "Reconnaissance des acquis de l'expérience (RAE)"
    RSFP = "RSFP", "Reconnaissance des savoir-faire professionnels (RSFP)"
    VAE = "VAE", "Validation des acquis de l'expérience (VAE)"
    AFEST = "AFEST", "Action de formation en situation de travail (AFEST)"
    OTHER = OTHER_CHOICE
    NONE = "NONE", "Aucune"


class SoftwareFinancialHelp(TextChoices):
    CNR = "CNR", "Les Crédits Non Reconductibles"
    FATESAT = "FATESAT", "Le FATESAT"
    CCAH = "CCAH", "Fonds CCAH (Comité National de Coordination Action Handicap)"
    DEDICATED_FUNDING = "DEDICATED_FUNDING", "Fonds spécifiques type AGGIRC-ARCO"
    OTHER = OTHER_CHOICE


class RetirementPreparationActions(TextChoices):
    ADMINISTRATIVE_ASSISTANCE = (
        "ADMINISTRATIVE_ASSISTANCE",
        "Accompagnement administratif (rendez-vous avec la CARSAT, aide à la préparation du dossier, informations sur les droits, etc.)",
    )
    UAAT = "UAAT", "Session de sensibilisation ou formation sur les droits à la retraite"
    MEETING_SCHEDULED = (
        "MEETING_SCHEDULED",
        "Organisation d'un RDV avec un professionnel compétent sur le sujet (Assistante sociale, RH, Directeur/-trice, etc.)",
    )
    PERSONAL_PLAN = "PERSONAL_PLAN", "Inscription dans le projet de la personne"
    CAF = "CAF", "Simulation de ressources auprès des services de la CAF"
    WORKING_HOURS_REDUCTION_AND_ORGANISATION = (
        "WORKING_HOURS_REDUCTION_AND_ORGANISATION",
        "Aménagement / réduction du temps de travail",
    )
    PSYCHOLOGICAL_AND_SOCIAL_ASSISTANCE = (
        "PSYCHOLOGICAL_AND_SOCIAL_ASSISTANCE",
        "Actions de transition psychologique et sociale",
    )
    OTHER = OTHER_CHOICE


class ESATAnswer(Answer):
    # ESATStep.INTRODUCTION
    finess_num = models.CharField(
        null=True,
        blank=True,
        max_length=9,
        validators=[validate_finess],
        verbose_name=get_field_text("esat-2025", "finess_num", "verbose_name"),
    )

    # ESATStep.ORGANIZATION
    esat_role = models.CharField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "esat_role", "verbose_name")
    )
    esat_name = models.CharField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "esat_name", "verbose_name")
    )
    esat_siret = models.CharField(
        null=True,
        blank=True,
        max_length=14,
        validators=[validate_siret],
        verbose_name=get_field_text("esat-2025", "esat_siret", "verbose_name"),
    )
    managing_organization_finess = models.CharField(
        null=True,
        blank=True,
        max_length=9,
        validators=[validate_finess],
        verbose_name=get_field_text("esat-2025", "managing_organization_finess", "verbose_name"),
    )
    esat_status = models.CharField(
        null=True,
        blank=True,
        choices=ESATLegalStatus.choices,
        verbose_name=get_field_text("esat-2025", "esat_status", "verbose_name"),
    )
    esat_dept = models.CharField(
        null=True,
        blank=True,
        choices=DEPARTMENTS.items(),
        verbose_name=get_field_text("esat-2025", "esat_dept", "verbose_name"),
    )

    nb_places_allowed = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name=get_field_text("esat-2025", "nb_places_allowed", "verbose_name"),
    )
    nb_employee_worked = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name=get_field_text("esat-2025", "nb_employee_worked", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_employee_worked", "help_text"),
    )
    nb_employee_shared = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name=get_field_text("esat-2025", "nb_employee_shared", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_employee_shared", "help_text"),
    )

    # ESATStep.WORKERS_SUPPORTED
    nb_worker_acc = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_acc", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_acc", "help_text"),
    )
    nb_worker_half_time = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_half_time", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_half_time", "help_text"),
    )
    mean_worker_age = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0), MaxValueValidator(80)],
        verbose_name=get_field_text("esat-2025", "mean_worker_age", "verbose_name"),
        help_text=get_field_text("esat-2025", "mean_worker_age", "help_text"),
    )
    mean_seniority = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0)],
        verbose_name=get_field_text("esat-2025", "mean_seniority", "verbose_name"),
        help_text=get_field_text("esat-2025", "mean_seniority", "help_text"),
    )

    # ESATStep.WORKERS_ENTRY
    nb_worker_previous_mot = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_previous_mot", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_previous_mot", "help_text"),
    )
    nb_worker_new = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_new", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_new", "help_text"),
    )
    nb_worker_temporary = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_temporary", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_temporary", "help_text"),
    )

    # ESATStep.ESTABLISHMENT_DISCOVERY
    nb_worker_mispe_mdph = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_mispe_mdph", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_mispe_mdph", "help_text"),
    )
    nb_worker_mispe_rpe = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_mispe_rpe", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_mispe_rpe", "help_text"),
    )

    # ESATStep.ORDINARY_WORKING_ENVIRONMENT
    nb_worker_willing_mot = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_willing_mot", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_willing_mot", "help_text"),
    )
    nb_worker_ft_job_seekers = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_ft_job_seekers", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_ft_job_seekers", "help_text"),
    )

    # ESATStep.ORDINARY_WORKING_ENVIRONMENT_AND_CUSTOMERS_INVOLVEMENT
    prescription_delegate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "prescription_delegate", "verbose_name"),
    )
    pmsmp_refused = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "pmsmp_refused", "verbose_name"),
    )
    nb_worker_pmsmp = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_pmsmp", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_pmsmp", "help_text"),
    )
    nb_worker_service = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_service", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_service", "help_text"),
    )
    nb_worker_mad_indiv = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_mad_indiv", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_mad_indiv", "help_text"),
    )
    nb_worker_with_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_with_public", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_with_public", "help_text"),
    )
    nb_worker_only_inside = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_only_inside", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_only_inside", "help_text"),
    )
    nb_worker_cumul_esat_ea = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_cumul_esat_ea", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_cumul_esat_ea", "help_text"),
    )
    nb_worker_cumul_esat_mot = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_cumul_esat_mot", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_cumul_esat_mot", "help_text"),
    )

    # ESATStep.WORKERS_LEFT
    nb_worker_left = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_left", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_left", "help_text"),
    )
    nb_worker_left_ea = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_left_ea", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_left_ea", "help_text"),
    )
    nb_worker_left_private = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_left_private", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_left_private", "help_text"),
    )
    nb_worker_left_asso = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_left_asso", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_left_asso", "help_text"),
    )
    nb_worker_left_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_left_public", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_left_public", "help_text"),
    )
    nb_worker_left_other_reason = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_left_other_reason", "verbose_name"),
    )
    nb_worker_cdi = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_cdi", "verbose_name"),
    )
    nb_worker_cdd = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_cdd", "verbose_name")
    )
    nb_worker_interim = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_interim", "verbose_name")
    )
    nb_worker_prof = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_prof", "verbose_name")
    )
    nb_worker_apprentice = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_apprentice", "verbose_name")
    )
    nb_conv_exit_agreement = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_conv_exit_agreement", "verbose_name"),
    )
    nb_conv_exit_agreement_new = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_conv_exit_agreement_new", "verbose_name"),
    )
    nb_worker_esrp = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_esrp", "verbose_name"),
    )

    # ESATStep.WORKERS_RIGHT_TO_RETURN
    nb_worker_reinteg = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_reinteg", "verbose_name")
    )
    nb_worker_reinteg_other = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_reinteg_other", "verbose_name")
    )
    nb_esat_agreement = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_esat_agreement", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_esat_agreement", "help_text"),
    )

    # ESATStep.SUPPORT_HOURS
    nb_support_hours = models.CharField(
        null=True,
        blank=True,
        choices=SupportHoursRange.choices,
        verbose_name=get_field_text("esat-2025", "nb_support_hours", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_support_hours", "help_text"),
    )
    support_themes = ArrayField(
        models.CharField(
            choices=SupportThemes.choices,
        ),
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "support_themes", "verbose_name"),
    )

    # ESATStep.FORMATIONS
    contrib_opco = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "contrib_opco", "verbose_name"),
    )
    pct_opco = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name=get_field_text("esat-2025", "pct_opco", "verbose_name"),
        help_text=get_field_text("esat-2025", "pct_opco", "help_text"),
    )
    nb_worker_formation_opco = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_formation_opco", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_formation_opco", "help_text"),
    )
    opco_or_anfh_refusal = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "opco_or_anfh_refusal", "verbose_name"),
    )
    nb_worker_cpf_unused = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_cpf_unused", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_cpf_unused", "help_text"),
    )
    cpf_unused_reason = models.TextField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "cpf_unused_reason", "verbose_name"),
    )
    formation_cpf = models.TextField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "formation_cpf", "verbose_name"),
    )
    nb_worker_intern_formation = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_intern_formation", "verbose_name"),
    )
    formation_subject = models.TextField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "formation_subject", "verbose_name")
    )
    autodetermination_formation = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "autodetermination_formation", "verbose_name"),
    )
    nb_worker_autodetermination = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_autodetermination", "verbose_name"),
    )
    autodetermination_external_formation = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "autodetermination_external_formation", "verbose_name"),
    )

    # ESATStep.SKILLS
    skills_validation_type = ArrayField(
        models.CharField(choices=SkillsValidationType.choices),
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "skills_validation_type", "verbose_name"),
    )
    nb_worker_rae_rsfp = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_rae_rsfp", "verbose_name"),
    )
    nb_worker_vae = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "nb_worker_vae", "verbose_name")
    )
    after_skills_validation = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "after_skills_validation", "verbose_name"),
    )

    # ESATStep.DUODAYS
    nb_worker_duoday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_duoday", "verbose_name"),
    )
    nb_employee_reverse_duoday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_employee_reverse_duoday", "verbose_name"),
    )

    # ESATStep.SKILLS_NOTEBOOK
    skills_notebook = models.CharField(
        null=True,
        blank=True,
        choices=YesNoWIP.choices,
        verbose_name=get_field_text("esat-2025", "skills_notebook", "verbose_name"),
    )
    software_financial_help = ArrayField(
        models.CharField(choices=SoftwareFinancialHelp.choices),
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "software_financial_help", "verbose_name"),
    )
    software_financial_help_type = models.TextField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "software_financial_help_type", "verbose_name")
    )

    # ESATStep.RETIREMENT
    retirement_preparation_actions = ArrayField(
        models.CharField(choices=RetirementPreparationActions.choices),
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "retirement_preparation_actions", "verbose_name"),
    )
    retirement_preparation_nb_workers = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "retirement_preparation_nb_workers", "verbose_name"),
    )
    uaat_inscription = models.CharField(
        null=True,
        blank=True,
        choices=YesNoWIP.choices,
        verbose_name=get_field_text("esat-2025", "uaat_inscription", "verbose_name"),
    )
    pct_more_than50 = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name=get_field_text("esat-2025", "pct_more_than50", "verbose_name"),
    )

    # ESATStep.LANGUAGE_ACCESSIBILITY
    documents_falclist = ArrayField(
        models.CharField(choices=DocumentFALCList.choices),
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "documents_falclist", "verbose_name"),
        help_text=get_field_text("esat-2025", "documents_falclist", "help_text"),
    )

    # ESATStep.WORKING_CONDITIONS
    worker_delegate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "worker_delegate", "verbose_name"),
    )
    worker_delegate_formation = models.CharField(
        null=True,
        blank=True,
        choices=[
            ("TRAINING_ORGANIZATION", "Par l'intermédiaire d'un organisme de formation"),
            ("INTERNALLY", "En interne"),
            NO_CHOICE,
        ],
        verbose_name=get_field_text("esat-2025", "worker_delegate_formation", "verbose_name"),
    )
    nb_delegate_hours = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_delegate_hours", "verbose_name"),
    )
    worker_delegate_hours_credit = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=get_field_text("esat-2025", "worker_delegate_hours_credit", "verbose_name")
    )
    mix_qvt_in_place = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "mix_qvt_in_place", "verbose_name"),
    )

    # ESATStep.PROFIT_SHARING
    profit_sharing_bonus = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "profit_sharing_bonus", "verbose_name"),
        help_text=get_field_text("esat-2025", "profit_sharing_bonus", "help_text"),
    )
    mean_pct_esat_rem = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name=get_field_text("esat-2025", "mean_pct_esat_rem", "verbose_name"),
        help_text=get_field_text("esat-2025", "mean_pct_esat_rem", "help_text"),
    )

    # ESATStep.INSURANCE_POLICY
    foresight_in_place = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "foresight_in_place", "verbose_name"),
    )
    year_foresight_in_place = models.CharField(
        null=True,
        blank=True,
        choices=[(str(year), year) for year in range(timezone.localdate().year, 1900, -1)] + [DO_NOT_KNOW_CHOICE],
        verbose_name=get_field_text("esat-2025", "year_foresight_in_place", "verbose_name"),
    )

    # ESATStep.MOBILITY_PROGRAM
    annual_transport_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "annual_transport_budget", "verbose_name"),
        help_text=get_field_text("esat-2025", "annual_transport_budget", "help_text"),
    )
    nb_worker_transport = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_transport", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_transport", "help_text"),
    )
    nb_worker_mobility_inclusion_card = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_mobility_inclusion_card", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_mobility_inclusion_card", "help_text"),
    )
    nb_worker_driving_licence = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_driving_licence", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_driving_licence", "help_text"),
    )
    nb_worker_code = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_code", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_worker_code", "help_text"),
    )

    # ESATStep.VOUCHERS
    holiday_voucher = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "holiday_voucher", "verbose_name"),
    )
    holiday_voucher_annual_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "holiday_voucher_annual_budget", "verbose_name"),
        help_text=get_field_text("esat-2025", "holiday_voucher_annual_budget", "help_text"),
    )
    gift_voucher = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "gift_voucher", "verbose_name"),
    )
    gift_voucher_annual_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "gift_voucher_annual_budget", "verbose_name"),
        help_text=get_field_text("esat-2025", "gift_voucher_annual_budget", "help_text"),
    )

    # ESATStep.SUNDAY_WORK
    nb_worker_worked_sunday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "nb_worker_worked_sunday", "verbose_name"),
    )

    # ESATStep.PARTNERSHIP_AGREEMENTS
    agreement_signed_ft = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "agreement_signed_ft", "verbose_name"),
    )
    agreement_signed_ea = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "agreement_signed_ea", "verbose_name"),
    )
    agreement_signed_dept_pae = models.BooleanField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "agreement_signed_dept_pae", "verbose_name"),
    )

    # ESATStep.STAFF
    nb_insertion_staff = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name=get_field_text("esat-2025", "nb_insertion_staff", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_insertion_staff", "help_text"),
    )
    nb_insertion_dispo = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name=get_field_text("esat-2025", "nb_insertion_dispo", "verbose_name"),
        help_text=get_field_text("esat-2025", "nb_insertion_dispo", "help_text"),
    )
    insertion_staff_funding = ArrayField(
        models.CharField(choices=BudgetFunding.choices),
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "insertion_staff_funding", "verbose_name"),
    )

    # ESATStep.COMMERCIAL_OPERATION
    annual_ca = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "annual_ca", "verbose_name"),
    )
    annual_ca_production = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "annual_ca_production", "verbose_name"),
    )
    annual_ca_service = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "annual_ca_service", "verbose_name"),
    )
    annual_ca_mad = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "annual_ca_mad", "verbose_name"),
    )
    pct_ca_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name=get_field_text("esat-2025", "pct_ca_public", "verbose_name"),
    )
    budget_commercial = models.CharField(
        null=True,
        blank=True,
        choices=BudgetState.choices,
        verbose_name=get_field_text("esat-2025", "budget_commercial", "verbose_name"),
    )
    budget_commercial_deficit = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name=get_field_text("esat-2025", "budget_commercial_deficit", "verbose_name"),
    )
    budget_commercial_excedent = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name=get_field_text("esat-2025", "budget_commercial_excedent", "verbose_name"),
    )

    # ESATStep.SOCIAL_ACTIVITY_BUDGET
    budget_social = models.CharField(
        null=True,
        blank=True,
        choices=BudgetState.choices,
        verbose_name=get_field_text("esat-2025", "budget_social", "verbose_name"),
        help_text=get_field_text("esat-2025", "budget_social", "help_text"),
    )
    budget_social_deficit = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name=get_field_text("esat-2025", "budget_social_deficit", "verbose_name"),
    )
    budget_social_excedent = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name=get_field_text("esat-2025", "budget_social_excedent", "verbose_name"),
    )

    # ESATStep.INVESTMENTS
    budget_accessibility = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "budget_accessibility", "verbose_name"),
    )
    budget_diversity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "budget_diversity", "verbose_name"),
    )

    # ESATStep.COMMENTS
    comments = models.TextField(
        null=True,
        blank=True,
        verbose_name=get_field_text("esat-2025", "comments", "verbose_name"),
    )

    # TODO: Delete the field when we don't need the date anymore
    # Per-step feedback (stored as JSON: {"step-name": "feedback text", ...})
    step_feedback = models.JSONField(null=True, blank=True, default=dict)

    class Meta:
        verbose_name = "réponse ESAT"
        verbose_name_plural = "réponses ESAT"
