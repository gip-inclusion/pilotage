# FIXME: Remove the noqa once the verbose_name are confirmed
# ruff: noqa: E501

import uuid_utils
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from django.utils.text import slugify

from pilotage.itoutils.departments import DEPARTMENTS
from pilotage.itoutils.validators import validate_finess, validate_siret


def _uuid7():
    # TODO: Replace by the stdlib function when moving to Python 3.14.
    return str(uuid_utils.uuid7())


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
    uid = models.UUIDField(primary_key=True, default=_uuid7, editable=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="answers", verbose_name="enquête")

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "réponse"

    def __str__(self):
        return str(self.uid)


DO_NOT_KNOW_VALUE = "DO_NOT_KNOW"
DO_NOT_KNOW_CHOICE = (DO_NOT_KNOW_VALUE, "Je ne sais pas")


class BudgetFunding(TextChoices):
    BPAS = "BPAS", "Par votre budget de fonctionnement (BPAS)"
    BAPC = "BAPC", "Par votre budget annexe de production et de commercialisation (BAPC)"


class BudgetState(TextChoices):
    SURPLUS = "SURPLUS", "excédentaire"
    BALANCE = "BALANCE", "à l'équilibre"
    DEFICIT = "DEFICIT", "déficitaire"
    DO_NOT_KNOW = DO_NOT_KNOW_VALUE, "Je ne sais pas"


class BudgetRange(TextChoices):
    LESS_THAN_100K = "LESS_THAN_100K", "Moins de 100 k€"
    RANGE_100K_500K = "RANGE_100K_500K", "100 k€ à 500k€"
    MORE_THAN_500K = "MORE_THAN_500K", "Plus de 500k€"
    DO_NOT_KNOW = DO_NOT_KNOW_VALUE, "Je ne sais pas"


class DocumentFALCList(TextChoices):
    CONTRACT = "CONTRACT", "Oui : contrat d'accompagnement par le travail"
    BOOKLET = "BOOKLET", "Oui : livret d'accueil"
    REGULATION = "REGULATION", "Oui : règlement de fonctionnement"
    NO = "NO", "Non"
    DO_NOT_KNOW = DO_NOT_KNOW_VALUE, "Je ne sais pas"


class ESATAnswer(Answer):
    # ESATStep.ORGANIZATION
    esat_role = models.CharField(null=True, blank=True, verbose_name="quelle est votre fonction au sein de l'ESAT ?")
    esat_name = models.CharField(null=True, blank=True, verbose_name="quel est le nom de votre ESAT ?")
    esat_siret = models.CharField(
        null=True,
        blank=True,
        max_length=14,
        validators=[validate_siret],
        verbose_name="quel est le numéro SIRET de l'ESAT ?",
    )
    finess_num = models.CharField(
        null=True,
        blank=True,
        max_length=9,
        validators=[validate_finess],
        verbose_name="quel est le numéro FINESS de l’établissement principal ?",
    )
    managing_organization_name = models.CharField(
        null=True, blank=True, verbose_name="quel est votre organisme gestionnaire ?"
    )
    esat_status = models.CharField(
        null=True,
        blank=True,
        choices=[("PUBLIC", "Public"), ("NON_PROFIT", "Privé sans but lucratif")],
        verbose_name="quel est le statut de l'ESAT ?",
    )
    esat_dept = models.CharField(
        null=True,
        blank=True,
        choices=DEPARTMENTS.items(),
        verbose_name="quel est le département d’implantation de l'ESAT ?",
    )

    nb_places_allowed = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="au 31 décembre n-1, quel était l'agrément fixé par l'ARS pour l'ESAT en nombre de places autorisées ?",
    )
    nb_employee_worked = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="combien de salarié(e)s ou d’agents publics (ESAT publics) ont travaillé dans l'ESAT ?",
        help_text="En équivalent temps plein (ETP), salariés ou agents publics encore en poste au 31/12/N-1 et ceux partis dans l'année",
    )

    # ESATStep.WORKERS_SUPPORTED
    nb_worker_acc = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses avez-vous accompagné ?",
        help_text="En nombre de travailleurs (effectif physique) en file active",
    )
    mean_worker_age = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0), MaxValueValidator(80)],
        verbose_name="au 31 décembre n-1, quel était l’âge moyen des travailleurs et travailleuses accompagnés ?",
        help_text="En nombre d'années",
    )
    mean_seniority = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0)],
        verbose_name="au 31 décembre n-1, quelle était l’ancienneté moyenne des travailleurs et travailleuses accompagnés ?",
        help_text="En nombre d'années",
    )
    nb_worker_half_time = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="parmi eux, combien de travailleurs et travailleuses étaient à temps partiel ?",
        help_text="En nombre de travailleurs (effectif physique) en file active",
    )

    # ESATStep.WORKERS_ENTRY
    nb_worker_previous_mot = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="quel était le nombre de travailleurs et travailleuses dans l'ESAT ayant occupé antérieurement à leur admission un emploi en milieu ordinaire y compris adapté ?",
        help_text="En nombre de travailleurs (effectif physique) parmi les travailleurs admis en n-1",
    )
    nb_worker_new = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="quel était le nombre de travailleurs et travailleuses dans l'ESAT admis pour la première fois en milieu protégé ?",
        help_text="En nombre de travailleurs (effectif physique) parmi les travailleurs admis en n-1",
    )
    nb_worker_temporary = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont été admis temporairement dans l'ESAT pour remplacer des travailleurs absents pour maladie, pour suivre une action formation ou pour occuper un emploi à temps partiel ?",
        help_text="En nombre de travailleurs (effectif physique) parmi les travailleurs admis en n-1",
    )

    # ESATStep.ESTABLISHMENT_DISCOVERY
    nb_worker_mispe_mdph = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par une MDPH ?",
        help_text="Nombre de personnes (effectif physique) accueillies en 2024",
    )
    nb_worker_mispe_rpe = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par le réseau pour l'emploi (RPE) ?",
        help_text="Nombre de personnes (effectif physique) accueillies en 2024",
    )

    # ESATStep.ORDINARY_WORKING_ENVIRONMENT
    nb_worker_willing_mot = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs de l'ESAT ont exprimé dans leur projet personnalisé leur volonté d’aller travailler en milieu ordinaire ?",
        help_text="Nombre de travailleurs",
    )
    nb_worker_ft_job_seekers = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses se sont inscrits comme demandeurs d’emploi à France Travail ?",
        help_text="Nombre de travailleurs parmi ceux ayant acté dans leur projet leur volonté d'aller vers le MOT",
    )

    # ESATStep.ORDINARY_WORKING_ENVIRONMENT_AND_CUSTOMERS_INVOLVEMENT
    prescription_delegate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="êtes-vous délégataire de prescription de PMSMP pour les travailleurs et travailleuses que vous accompagnez ?",
    )
    pmsmp_refused = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="avez-vous eu des refus de PMSMP par les organismes du réseau pour l'emploi (France Travail, Cap Emploi, Mission Locale) pour un ou plusieurs de vos travailleurs et travailleuses ?",
    )
    nb_worker_pmsmp = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="combien de travailleurs et travailleuses ont effectué une PMSMP ?"
    )
    nb_worker_service = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont réalisé une prestation de service auprès d'une entreprise, d'une collectivité publique ou de tout autre organisme, assurée avec ou un plusieurs salarié(e)s de l'ESAT ?",
    )
    nb_worker_mad_indiv = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition individuelle d'un employeur public ou privé ?",
    )
    nb_worker_mad_collec = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition collective d'un employeur public ou privé ?",
    )
    nb_worker_with_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="nombre de travailleur et travailleuses ayant réalisé une activité dans un lieu au contact de la clientèle ?",
    )
    nb_worker_only_inside = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="nombre de travailleur et travailleuses étant resté travailler dans les murs sans contact avec le public ou le MOT",
    )
    pct_activity_outside = models.CharField(
        null=True,
        blank=True,
        choices=[
            ("0-20", "De 0% à 20%"),
            ("21-40", "De 21% à 40%"),
            ("41-60", "De 41% à 60%"),
            ("61-80", "De 61% à 80%"),
            ("81-100", "De 81 à 100%"),
            DO_NOT_KNOW_CHOICE,
        ],
        verbose_name="sur l’ensemble de l’activité de l’ESAT, quel est le pourcentage d’activité exercée en dehors de l’établissement ?",
    )
    nb_worker_cumul_esat_ea = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT et un emploi à temps partiel en Entreprise Adaptée ?",
    )
    nb_worker_cumul_esat_mot = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT avec un emploi à temps partiel en milieu ordinaire classique, privé ou public ?",
    )

    # ESATStep.WORKERS_LEFT
    nb_worker_left = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="en n-1, combien de travailleurs et travailleuses ont quitté l'ESAT ?",
        help_text="Nombre de travailleurs partis au cours de l'année N-1",
    )
    nb_worker_left_ea = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien ont quitté l'ESAT pour un emploi en entreprise adaptée ?",
        help_text="Y compris intérim",
    )
    nb_worker_left_private = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé lucratif ?",
        help_text="Y compris intérim",
    )
    nb_worker_left_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire public ?",
        help_text="Y compris intérim",
    )
    nb_worker_left_asso = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé non lucratif (associations) ?",
        help_text="Y compris intérim",
    )
    nb_worker_left_other_reason = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien ont quitté l'ESAT pour d'autres raisons ?",
    )
    nb_worker_cdi = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="parmi eux, combien ont signé un CDI ?"
    )
    nb_worker_cdd = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="parmi eux, combien ont signé un CDD ?"
    )
    nb_worker_interim = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="parmi eux, combien ont signé en mission d'interim ?"
    )
    nb_worker_prof = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="parmi eux, combien ont signé un contrat de professionnalisation ?"
    )
    nb_worker_apprentice = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="parmi eux, combien ont signé un contrat d'apprentissage ?"
    )
    nb_conv_exit_agreement = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de conventions d'appui sont actuellement en vigueur dans l'ESAT avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d’un travailleur en milieu ordinaire au 31/12/N-1 ?",
    )
    nb_conv_exit_agreement_new = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de conventions d'appui ont été signées dans l'année N-1 avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d’un travailleur en milieu ordinaire ?",
    )
    nb_worker_esrp = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont suivi une formation en établissement et service de réadaptation professionnelle (ESRP) ?",
    )

    # ESATStep.WORKERS_RIGHT_TO_RETURN
    nb_worker_reinteg = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="nombre de travailleurs et travailleuses ayant réintégrés l'ESAT"
    )
    nb_worker_reinteg_other = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="nombre de travailleurs et travailleuses ayant intégrés un autre ESAT"
    )
    nb_worker_other_esat_with_agreement = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="parmi eux, combien ont réintégré un ESAT avec lequel vous aviez conclu une convention de retour ?",
        help_text="Nombre de travailleurs",
    )
    nb_esat_agreement = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="avec combien d'ESAT avez-vous conventionné pour garantir l’exercice du droit au retour ?",
        help_text="Nombre d'ESAT",
    )

    # ESATStep.SUPPORT_HOURS
    nb_support_hours = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="quel était le nombre d’heures de soutien liées à l’activité professionnelle, dont en moyenne chaque travailleur a bénéficié (rémunérées et comprises dans le temps de travail) ?",
        help_text="Nombre d'heures en moyenne par travailleur sur année n-1",
    )
    support_themes = models.TextField(null=True, blank=True, verbose_name="sur quelles thématiques principales ?")

    # ESATStep.FORMATIONS
    contrib_opco = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="est-ce que l'ESAT a acquitté une contribution pour la formation de vos travailleurs et travailleuses auprès de l’OPCO Santé ou de l’OPCA ANFH (pour les ESAT publics) ?",
    )
    pct_opco = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="quel a été le taux de votre contribution à l’OPCO Santé ou à l’ANFH ?",
        help_text="en %",
    )
    nb_worker_formation_opco = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont suivi une formation prise en charge par l'OPCO Santé ou par l’ANFH ?",
        help_text="Nombre de travailleurs en file active",
    )
    opco_or_anfh_refusal = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="l'ESAT a –t-il fait l’objet d’un ou plusieurs refus de financement d’une formation par l’OPCO Santé ou l’ANFH ?",
    )
    nb_worker_cpf_unused = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="au 31 décembre n-1, et depuis leur admission dans l'ESAT, combien de travailleurs et travailleuses ont utilisé leur CPF ?",
        help_text="Nombre de travailleurs en file active",
    )
    cpf_unused_reason = models.TextField(
        null=True,
        blank=True,
        verbose_name="pour quelles raisons les travailleurs et travailleurs n'utilisent pas leur CPF ?",
    )
    formation_cpf = models.TextField(
        null=True,
        blank=True,
        verbose_name="quelle a été la formation majoritairement suivie par les travailleurs et travailleuses de l'ESAT au titre de leur CPF ?",
    )
    nb_worker_intern_formation = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'au moins une formation animée en interne par les salarié(e)s de l'ESAT ?",
    )
    formation_subject = models.TextField(
        null=True, blank=True, verbose_name="quels ont été les sujets des formation dispensés par l’ESAT ?"
    )
    autodetermination_formation = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="avez-vous mis en place une formation à l'autodétermination pour les travailleurs et travailleuses ?",
    )
    nb_worker_autodetermination = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont bénéficié dans l'année d’une formation à l’autodétermination ?",
    )
    autodetermination_external_formation = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="la formation à l'autodétermination pour les travailleuses et travailleurs est-elle assurée par l'intermédiaire d'un organisme de formation ?",
    )

    # ESATStep.SKILLS
    skills_validation_type = models.TextField(
        null=True,
        blank=True,
        verbose_name="quels ont été les types de dispositifs dont ont bénéficié les travailleurs et travailleuses de l'ESAT pour reconnaitre et développer leurs compétences ?",
    )
    nb_worker_rae_rsfp = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont bénéficié d’une RAE ou d’une RSFP ?",
    )
    nb_worker_vae = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="combien de travailleurs et travailleuses ont bénéficié d’une VAE ?"
    )
    after_skills_validation = models.CharField(
        null=True,
        blank=True,
        choices=[
            ("NO_CHANGES", "Maintien sur l’activité professionnelle initiale au sein de l'ESAT"),
            ("OTHER_ACTIVITY", "Accès à d’autres activités professionnelles au sein de l'ESAT"),
            ("OTHER_ESAT", "Changement d’ESAT"),
            ("ESRP", "Accès à une formation via un établissement ou service de réadaptation professionnelle (ESRP)"),
            ("TRAINING_COURSE", "Accès à une formation via un organisme de formation"),
            ("PARTIAL_TIME_WORK", "Accès à un emploi via le temps partagé"),
            ("LEFT", "Sortie de l'ESAT pour accéder à un emploi en milieu ordinaire ou adapté"),
            DO_NOT_KNOW_CHOICE,
        ],
        verbose_name="a l’issue de cette reconnaissance ou validation, quelle a été la suite du parcours des travailleurs et travailleuses concerné(e)s ?",
    )

    # ESATStep.DUODAYS
    nb_worker_duoday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont participé à Duoday ?",
    )
    nb_employee_reverse_duoday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="en n-1, combien de professionnels du milieu ordinaire ont participé à des Duoday inversés ?",
    )

    # ESATStep.SKILLS_NOTEBOOK
    skills_notebook = models.BooleanField(
        null=True, blank=True, verbose_name="avez-vous mis en place un carnet de parcours et de compétences ?"
    )
    skills_notebook_software_used = models.TextField(
        null=True,
        blank=True,
        verbose_name="avez-vous utilisé un logiciel spécifique pour mettre en place le carnet, et si oui lequel ?",
    )
    software_name = models.TextField(
        null=True,
        blank=True,
        verbose_name="logiciel utilisé",
    )
    software_financial_help = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="l'ESAT a t-il bénéficié d’une aide financière pour mettre en place ce carnet et le cas échéant, acquérir un logiciel ?",
    )
    software_financial_help_type = models.TextField(null=True, blank=True, verbose_name="type d'aide")

    # ESATStep.RETIREMENT
    retirement_preparation_actions = models.TextField(
        null=True,
        blank=True,
        verbose_name="quelles ont été les actions conduites par l'ESAT pour préparer les travailleurs et travailleuses au départ à la retraite (inscription dans la démarche Un Avenir Après le Travail, rendez-vous organisés avec la CARSAT, etc.) ?",
    )
    uaat_inscription = models.CharField(
        null=True,
        blank=True,
        choices=[("YES", "Oui"), ("NO", "Non"), ("IN_PROGRESS", "en cours d'inscription"), DO_NOT_KNOW_CHOICE],
        verbose_name="etes-vous inscrit dans la démarche Un Avenir Après le Travail (UAAT) ?",
    )
    retirement_preparation_nb_workers = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont bénéficié d’actions de préparation à la retraite, dans le cadre ou non d’Un Avenir Après le Travail ?",
    )
    pct_more_than50 = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="combien de travailleur.euse.s de plus de 50 ans ?",
    )

    # ESATStep.LANGUAGE_ACCESSIBILITY
    documents_falclist = ArrayField(
        models.CharField(choices=DocumentFALCList.choices),
        null=True,
        blank=True,
        verbose_name="au 31 décembre N-1, les principaux documents destinés aux travailleurs et travailleuses étaient-ils accessibles en FALC ou en communication alternative augmentée ? (contrat d’accompagnement par le travail, livret d’accueil, règlement de fonctionnement, etc.)",
        help_text="Le facile à lire et à comprendre (FALC) est une méthode qui a pour but de traduire un langage classique en un langage simplifié.",
    )

    # ESATStep.WORKING_CONDITIONS
    worker_delegate = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="en n-1, y-a-t-il dans l'ESAT un délégué/une déléguée des travailleurs élu(e) ?",
    )
    worker_delegate_formation = models.CharField(
        null=True,
        blank=True,
        choices=[
            ("TRAINING_ORGANIZATION", "par l'intermédiaire d'un organisme de formation"),
            ("INTERNALLY", "en interne"),
            DO_NOT_KNOW_CHOICE,
        ],
        verbose_name="est-ce que le délégué ou la déléguée a bénéficié d'une formation au cours de son mandat pour cette mission :",
    )
    worker_delegate_hours_credit = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="est-ce que le délégué ou la déléguée bénéficie d'un crédit d'heures chaque mois pour remplir sa mission ?",
    )
    nb_delegate_hours = models.BooleanField(
        null=True, blank=True, verbose_name="si oui, précisez le nombre d'heures", help_text="Nombre d'heures par mois"
    )
    mix_qvt_in_place = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="une instance mixte (salarié(e)s/travailleurs et travailleuses) sur la qualité de vie au travail (QVT), l’hygiène et la sécurité et l’évaluation des risques professionnels a-t-elle été mise en place ?",
    )

    # ESATStep.PROFIT_SHARING
    profit_sharing_bonus = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="en n-1, quel était le montant moyen de la prime d’intéressement (au sens de l’article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
    )
    mean_pct_esat_rem = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="au 31 décembre n-1, quel était le montant moyen de la part rémunération garantie du travailleur prise en charge financièrement par l'ESAT (en pourcentage du SMIC)?",
    )

    # ESATStep.INSURANCE_POLICY
    foresight_in_place = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="est-ce que l'ESAT a contribué en n-1 à un régime de prévoyance au sens de l’article R 243-9 du CASF, avec compensation par l’Etat d’une partie de la contribution ?",
    )
    year_foresight_in_place = models.CharField(
        null=True,
        blank=True,
        choices=[(str(year), year) for year in range(timezone.localdate().year, 1900, -1)] + [DO_NOT_KNOW_CHOICE],
        verbose_name="depuis quelle année ce régime de prévoyance est-il mis en œuvre dans l'ESAT ?",
    )

    # ESATStep.MOBILITY_PROGRAM
    annual_transport_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="quel budget annuel avez-vous alloué au transport des travailleurs et travailleuses de leur domicile à l’ESAT (transport en commun et/ou navette et/ou taxi) en euro ?",
    )
    nb_worker_transport = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'un transport proposé par l'ESAT? (transport en commun et/ou navette et/ou taxi)",
    )
    nb_worker_mobility_inclusion_card = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses ont bénéficié de la carte mobilité inclusion ?",
    )
    nb_worker_driving_licence = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="combien de travailleurs et travailleuses ont leur permis de conduire ?"
    )
    nb_worker_code = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="combien de travailleurs et travailleuses ont le code ?"
    )

    # ESATStep.VOUCHERS
    holiday_voucher = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="l'ESAT propose-t-il des chèques vacances aux travailleurs et travailleuses ?",
    )
    holiday_voucher_annual_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="quel est le budget annuel de l'ESAT pour les chèques vacances ?",
        help_text="En euros",
    )
    gift_voucher = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="l'ESAT propose-t-il des chèques cadeaux aux travailleurs et travailleuses ?",
    )
    gift_voucher_annual_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="quel est le budget annuel de l'ESAT pour les chèques cadeaux ?",
        help_text="En euros",
    )

    # ESATStep.SUNDAY_WORK
    nb_worker_worked_sunday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="combien de travailleurs et travailleuses de l'ESAT ont travaillé au moins un dimanche ou un jour férié en n-1 ?",
    )

    # ESATStep.PARTNERSHIP_AGREEMENTS
    rpe_agreement_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="avez-vous signé en n-1 une convention de partenariat territoriale avec le réseau pour l’emploi ?",
    )
    pea_agreement_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="avez-vous signé en n-1 une convention de partenariat avec une Plateforme Emploi Accompagné ?",
    )
    esat_pea_rattached = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="êtes-vous un ESAT porteur ou rattaché à une structure qui gère une plateforme d’emploi accompagné (en tant que signataire de la convention de gestion)  ?",
    )
    ea_convention_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="avez-vous signé en n-1 une convention de partenariat avec une entreprise adaptée (EA)  ?",
    )
    nb_ea_convention_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="avec combien d'entreprises adaptées présentes sur votre territoire avez-vous une convention de partenariat au 31 décembre n-1 ?",
    )

    # ESATStep.STAFF
    nb_insertion_staff = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont dans vos effectifs ?",
        help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP",
    )
    nb_insertion_dispo = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont mis à disposition ou mutualisés ?",
        help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP",
    )
    insertion_staff_funding = models.CharField(
        null=True,
        blank=True,
        choices=BudgetFunding.choices,
        verbose_name="comment sont-ils financés ?",
    )

    # ESATStep.COMMERCIAL_OPERATION
    annual_ca = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="quel était votre chiffre d'affaire annuel commercial tout confondu (productions propres, prestations de service, mises à disposition de travailleurs et travailleuses auprès d’utilisateurs) ?",
    )
    annual_ca_production = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="quel était votre chiffre d'affaire annuel commercial en productions propres ?",
    )
    annual_ca_service = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="quel était votre chiffre d'affaire annuel commercial en prestation de service ?",
    )
    annual_ca_mad = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="quel est le montant annuel de votre chiffre d'affaires (Compte 706) issu exclusivement des contrats de mise à disposition de travailleurs et travailleuses handicapés (MAD) auprès d'utilisateurs tiers (entreprises, collectivités, associations) ?",
    )
    pct_ca_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="indiquez le pourcentage de votre chiffre d'affaires réalisé avec des clients du secteur public",
    )
    budget_commercial = models.CharField(
        null=True, blank=True, choices=BudgetState.choices, verbose_name="sur le résultat net de la SEC, étiez-vous"
    )
    budget_commercial_deficit = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="de quel montant est-ce déficit ?",
    )
    budget_commercial_excedent = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="de quel montant est-cet excédant?",
    )

    # ESATStep.SOCIAL_ACTIVITY_BUDGET
    budget_social = models.CharField(
        null=True,
        blank=True,
        choices=BudgetState.choices,
        verbose_name="sur le résultat de clôture de votre Budget de Fonctionnement (Section d'Exploitation du Budget Social), étiez-vous :",
        help_text="Budget de fonctionnement dit aussi budget social",
    )
    budget_social_deficit = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="de quel montant est-ce déficit ?",
    )
    budget_social_excedent = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="de quel montant est-cet excédant?",
    )

    # ESATStep.INVESTMENTS
    budget_accessibility = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="quel a été le montant des investissements de mise aux normes de sécurité et d’accessibilité des installations réalisés par l'ESAT en n-1 ?",
    )
    budget_diversity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="quel a été le montant des investissements permettant de diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en n-1 ?",
    )

    # ESATStep.COMMENTS
    comments = models.TextField(
        null=True,
        blank=True,
        verbose_name="nous arrivons à la fin du questionnaire - merci d'avoir pris le temps de le remplir.  Commentaires",
    )

    class Meta:
        verbose_name = "réponse ESAT"
        verbose_name_plural = "réponses ESAT"
