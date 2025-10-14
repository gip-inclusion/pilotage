# FIXME: Remove the noqa once the verbose_name are confirmed
# ruff: noqa: E501

import uuid_utils
from django.contrib.postgres.fields import ArrayField
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


class Survey(models.Model):
    kind = models.CharField(verbose_name="type", choices=SurveyKind.choices)
    vintage = models.CharField(verbose_name="millésime")
    name = models.SlugField(verbose_name="nom", unique=True, editable=False)

    introduction = models.fields.TextField(null=True, blank=True)
    conclusion = models.fields.TextField(null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "enquête"

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.name or slugify(f"{self.kind} {self.vintage}")
        super().save(**kwargs)


class AnswerStatus(models.TextChoices):
    PENDING = "pending", "en cours"
    DONE = "done", "terminé"


class Answer(models.Model):
    uid = models.UUIDField(primary_key=True, default=_uuid7, editable=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="answers", verbose_name="enquête")
    status = models.CharField(verbose_name="statut", default=AnswerStatus.PENDING, choices=AnswerStatus.choices)

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "réponse"

    def __str__(self):
        return str(self.uid)


DO_NOT_KNOW_VALUE = "DO_NOT_KNOW"
DO_NOT_KNOW_CHOICE = (DO_NOT_KNOW_VALUE, "Je ne sais pas")


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
    esat_role = models.CharField(null=True, blank=True, verbose_name="Quelle est votre fonction au sein de l'ESAT ?")
    esat_name = models.CharField(null=True, blank=True, verbose_name="Quel est le nom de votre ESAT ?")
    esat_siret = models.CharField(
        null=True,
        blank=True,
        max_length=14,
        validators=[validate_siret],
        verbose_name="Quel est le numéro SIRET de l'ESAT ?",
    )
    finess_num = models.CharField(
        null=True,
        blank=True,
        max_length=9,
        validators=[validate_finess],
        verbose_name="Quel est le numéro FINESS de l’établissement principal ?",
    )
    managing_organization_name = models.CharField(
        null=True, blank=True, verbose_name="Quel est votre organisme gestionnaire ?"
    )
    esat_status = models.CharField(
        null=True,
        blank=True,
        choices=[("PUBLIC", "Public"), ("NON_PROFIT", "Privé sans but lucratif")],
        verbose_name="Quel est le statut de l'ESAT ?",
    )
    esat_dept = models.CharField(
        null=True,
        blank=True,
        choices=DEPARTMENTS.items(),
        verbose_name="Quels est le département d’implantation de l'ESAT ?",
    )

    # ESATStep.EMPLOYEE
    nb_places_allowed = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="Au 31 décembre 2024, quel était le nombre de places autorisées par l’ARS pour l'ESAT ?",
    )
    nb_employee_worked = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=4,
        validators=[MinValueValidator(0)],
        verbose_name="Combien de salarié(e)s ou d’agents publics (ESAT publics) ont travaillé dans l'ESAT?",
    )
    nb_employee_acc = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Combien de travailleurs et travailleuses avez-vous accompagné ?"
    )
    mean_employee_age = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0), MaxValueValidator(80)],
        verbose_name="Quel était l’âge moyen des travailleurs et travailleuses accompagnés ?",
    )
    mean_seniority = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=1,
        max_digits=3,
        validators=[MinValueValidator(0)],
        verbose_name="Quelle était l’ancienneté moyenne des travailleurs et travailleuses accompagnés ?",
        help_text="L'ancienneté moyenne doit être exprimée en mois",
    )
    nb_employee_ordinary_job = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était le nombre de travailleurs et travailleuses dans l'ESAT ayant occupé antérieurement à leur admission un emploi en milieu ordinaire y compris adapté ?",
    )
    nb_employee_new = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était le nombre de travailleurs et travailleuses dans l'ESAT admis pour la première fois en milieu protégé ?",
    )
    nb_employee_temporary = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont été admis temporairement dans l'ESAT pour remplacer des travailleurs absents pour maladie, pour suivre une action formation ou pour occuper un emploi à temps partiel ?",
        help_text="et maintenir ainsi votre capacité d’activité en bénéficiant via l’ASP de l’annualisation de l’aide au poste",
    )
    nb_employee_willing_ordinary = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs de l'ESAT ont exprimé dans leur projet personnalisé leur volonté d’aller travailler en milieu ordinaire ?",
    )
    nb_employee_ft_job_seekers = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses se sont inscrits comme demandeurs d’emploi à France Travail ? ",
    )
    nb_employee_mispe_mdph = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par une MDPH ?",
    )
    nb_employee_mispe_rpe = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par le réseau pour l'emploi (RPE) ?",
    )

    # ESATStep.PMSMP
    prescription_delegate = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Êtes-vous délégataire de prescription de PMSMP pour les travailleurs et travailleuses que vous accompagnez ?",
    )
    pmsmp_refused = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Avez-vous eu des refus de PMSMP par les organismes du réseau pour l'emploi (France Travail, Cap Emploi, Mission Locale) pour un ou plusieurs de vos travailleurs et travailleuses ?",
    )
    nb_employee_pmsmp = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs et travailleuses ayant effectué une PMSMP"
    )

    # ESATStep.ACTIVITY_KIND
    nb_employee_service = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nombre de travailleurs et travailleuses ayant réalisé une prestation de service auprès d'une entreprise, d'une collectivité publique ou de tout autre organisme, assurée avec ou un plusieurs salarié(e)s de l'ESAT",
    )
    nb_employee_dispo_indiv = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nombre de travailleurs et travailleuses ayant réalisé une mise à disposition individuelle d'un employeur public ou privé",
    )
    nb_employee_dispo_collec = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nombre de travailleurs et travailleuses ayant réalisé une mise à disposition collective d'un employeur public ou privé",
    )
    nb_employee_restau = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nombre de travailleurs et travailleuses ayant réalisé une activité en boutique/restaurant",
    )
    nb_employee_worked_sunday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses de l'ESAT ont travaillé au moins un dimanche ou un jour férié en 2024 ?",
    )

    # ESATStep.PARTIAL_WORK
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
        verbose_name="Sur l’ensemble de l’activité de l’ESAT, quel est le pourcentage d’activité exercée en dehors de l’établissement ?",
    )
    nb_employee_half_time = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Parmi eux, combien de travailleurs et travailleuses étaient à temps partiel ?",
        help_text="hors situation de temps partagé entre milieu protégé et milieu ordinaire",
    )
    nb_employee_cumul_esat_ea = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT et un emploi à temps partiel en Entreprise Adaptée ?",
        help_text="Ici, il ne faut pas comptabiliser par contrat mais par travailleur",
    )
    nb_employee_cumul_esat_ordi = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT avec un emploi à temps partiel en milieu ordinaire classique, privé ou public ?",
        help_text="Ici, il ne faut pas comptabiliser par contrat mais par travailleur",
    )

    # ESATStep.EMPLOYEE_LEFT
    nb_employee_left = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="combien de travailleurs et travailleuses ont quitté l'ESAT ?"
    )
    nb_employee_left_ea = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="nombre de travailleurs en entreprise adaptée"
    )
    nb_employee_left_private = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="nombre de travailleurs dans le privé"
    )
    nb_employee_left_public = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="nombre de travailleurs dans le public"
    )
    nb_employee_left_asso = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="nombre de travailleurs en association"
    )
    nb_employee_cdi = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs ayant signé un CDI"
    )
    nb_employee_cdd = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs ayant signé un CDD"
    )
    nb_employee_interim = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs en  missions Interim"
    )
    nb_employee_prof = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs en contrat de professionnalisation"
    )
    nb_employee_apprentice = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs en contrat d'apprentissage"
    )

    # ESATStep.EMPLOYEE_RETURN
    nb_employee_reinteg = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs et travailleuses ayant réintégrés l'ESAT"
    )
    nb_employee_reinteg_other = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Nombre de travailleurs et travailleuses ayant intégrés un autre ESAT"
    )
    nb_esat_conv = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Avec combien d'ESAT avez-vous conventionné pour garantir l’exercice du droit au retour ?",
    )

    # ESATStep.MISC
    nb_conv_exit = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de conventions d'appui ont été conclues dans l'ESAT avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d’un travailleur en milieu ordinaire ?",
    )
    nb_employee_left_esrp = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont quitté l’ESAT pour suivre une formation en établissement et service de réadaptation professionnelle (ESRP) ?",
    )
    nb_support_hours = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était le nombre d’heures de soutien liées à l’activité professionnelle, dont en moyenne chaque travailleur a bénéficié (rémunérées et comprises dans le temps de travail) ?",
    )
    support_themes = models.TextField(null=True, blank=True, verbose_name="Sur quelles thématiques principales?")

    # ESATStep.EMPLOYEE_RETIREMENT
    retirement_preparation = models.TextField(
        null=True,
        blank=True,
        verbose_name="Quelles ont été les actions conduites par l'ESAT pour préparer les travailleurs et travailleuses au départ à la retraite (inscription dans la démarche Un Avenir Après le Travail, rendez-vous organisés avec la CARSAT, etc.) ?",
    )
    uaat_inscription = models.CharField(
        null=True,
        blank=True,
        choices=[("YES", "Oui"), ("NO", "Non"), ("IN_PROGRESS", "En cours"), DO_NOT_KNOW_CHOICE],
        verbose_name="Etes-vous inscrit dans la démarche Un Avenir Après le Travail (UAAT) ?",
    )
    nb_uaat_beneficiary = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont bénéficié d’actions de préparation à la retraite, dans le cadre ou non d’Un Avenir Après le Travail ?",
    )
    pct_more_than50 = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="Quelle proportion de travailleurs et travailleuses de plus de 50 ans cela représente ?",
    )

    # ESATStep.OPCO
    contrib_opco = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Est-ce que l'ESAT a acquitté une contribution pour la formation de vos travailleurs et travailleuses auprès de l’OPCO Santé ou de l’OPCA ANFH (pour les ESAT publics) ?",
    )
    pct_opco = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="Quel a été le taux de votre contribution à l’OPCO Santé ou à l’ANFH ?",
        help_text="En pourcentage de l’assiette de contribution",
    )
    nb_employee_formation_opco = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="En 2024, combien de travailleurs et travailleuses de l'ESAT ont suivi une formation prise en charge par l'OPCO Santé ou par l’ANFH ?",
    )
    opco_or_anfh_refusal = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="L'ESAT a –t-il fait l’objet d’un ou plusieurs refus de financement d’une formation par l’OPCO Santé ou l’ANFH ?",
    )

    # ESATStep.SKILLS
    nb_employee_rae = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont bénéficié d’une RAE ou d’une RSFP ?",
    )
    nb_employee_rsfp = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Combien de travailleurs et travailleuses ont bénéficié d’une VAE ?"
    )
    after_reco_situation_list = models.CharField(
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
        verbose_name="A l’issue de cette reconnaissance ou validation, quelle a été la suite du parcours des travailleurs et travailleuses concerné(e)s ?",
    )

    # ESATStep.CPF
    nb_employeed_cpf_unused = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Au 31 décembre 2024, et depuis leur admission dans l'ESAT, combien de travailleurs et travailleuses n'ont pas encore utilisé leur CPF ?",
    )
    cpfreason = models.TextField(null=True, blank=True, verbose_name="Pour quelles raisons?")
    formation_cpf = models.TextField(
        null=True,
        blank=True,
        verbose_name="Quelle a été la formation majoritairement suivie par les travailleurs et travailleuses de l'ESAT au titre de leur CPF ?",
    )

    # ESATStep.AUTODETERMINATION
    nb_employee_intern_formation = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont bénéficié d'au moins une formation animée en interne par les salarié(e)s de l'ESAT ?",
    )
    formation_subject = models.TextField(
        null=True, blank=True, verbose_name="Quels ont été les sujets des formation dispensés par l’ESAT ?"
    )
    autodetermination_formation = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Avez-vous mis en place une formation à l'autodétermination pour les travailleurs et travailleuses?",
    )
    nb_employee_autodetermination = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont bénéficié d’une formation à l’autodétermination ?",
    )
    autodetermination_external_formation = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="La formation à l'autodétermination pour les travailleuses et travailleurs est-elle assurée par l'intermédiaire d'un organisme de formation ?",
    )

    # ESATStep.DUODAY
    nb_employee_duoday = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="En 2024, combien de travailleurs et travailleuses de l'ESAT ont participé à Duoday ?",
    )
    duoday_board = models.BooleanField(
        null=True, blank=True, verbose_name="Avez-vous mis en place un carnet de parcours et de compétences ?"
    )
    duoday_software_used = models.TextField(
        null=True,
        blank=True,
        verbose_name="Avez-vous utilisé un logiciel spécifique pour mettre en place le carnet, et si oui lequel ?",
    )
    duoday_software_financial_help = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="L'ESAT a t-il bénéficié d’une aide financière pour mettre en place ce carnet et le cas échéant, acquérir un logiciel ?   ",
    )
    duoday_financial_help_type = models.TextField(null=True, blank=True, verbose_name="Type d'aide")

    # ESATStep.REPRESENTATIVE
    documents_falclist = ArrayField(
        models.CharField(choices=DocumentFALCList.choices),
        null=True,
        blank=True,
        verbose_name="Au 31 décembre 2024, les principaux documents destinés aux travailleurs et travailleuses étaient-ils accessibles en FALC ou en communication alternative augmentée?(contrat d’accompagnement par le travail, livret d’accueil, règlement de fonctionnement, etc.)",
        help_text="Le facile à lire et à comprendre (FALC) est une méthode qui a pour but de traduire un langage classique en un langage simplifié.",
    )
    employee_delegate = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="En 2024, y-a-t-il dans l'ESAT un délégué/une déléguée des travailleurs élu(e) ?",
    )
    employee_delegate_formation = models.CharField(
        null=True,
        blank=True,
        choices=[
            ("TRAINING_ORGANIZATION", "par l'intermédiaire d'un organisme de formation"),
            ("INTERNALLY", "en interne"),
            DO_NOT_KNOW_CHOICE,
        ],
        verbose_name="Est-ce que le délégué ou la déléguée a bénéficié d'une formation :",
    )
    employee_delegate_hours_credit = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Est-ce que le délégué ou la déléguée bénéficie d'un crédit d'heures chaque mois pour remplir sa mission?",
    )
    nb_delegate_hours = models.BooleanField(null=True, blank=True, verbose_name="Si oui, précisez le nombre d'heures")
    mix_qvt_in_place = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Une instance mixte (salarié(e)s/travailleurs et travailleuses) sur la qualité de vie au travail (QVT), l’hygiène et la sécurité et l’évaluation des risques professionnels a-t-elle été mise en place?",
    )

    # ESATStep.BONUS
    profit_sharing_bonus = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="En 2024, quel était le montant moyen de la prime d’intéressement (au sens de l’article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
        help_text="Possibilité de mettre 0",
    )
    mean_pct_esat_rem = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="Au 31 décembre 2024, quel était le montant moyen de la part rémunération garantie du travailleur prise en charge financièrement par l'ESAT (en pourcentage du SMIC)?",
    )
    pct_employee_activity_bonus = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="Quel pourcentage de travailleurs et travailleuses bénéficie de la prime d'activité?",
    )

    # ESATStep.HEALTH_ASSURANCE
    health_complementary = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Les travailleurs et travailleuses de l’ESAT bénéficiaient-ils en 2024 d’une complémentaire santé collective avec prise en charge par l’ESAT d’une partie du coût de la cotisation ? ",
    )
    pct_health_complementary_esat = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="Quel était le pourcentage de financement par l'ESAT en 2024 ?",
        help_text="Possibilité de mettre 0",
    )
    annual_health_complementary_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était le montant annuel pour 2024 pour l'ensemble des travailleurs et travailleuses couverts de la contribution acquittée par l’ESAT ?",
    )
    foresight_in_place = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Est-ce que l'ESAT a contribué en 2024 à un régime de prévoyance au sens de l’article R 243-9 du CASF, avec compensation par l’Etat d’une partie de la contribution?",
    )
    year_foresight_in_place = models.CharField(
        null=True,
        blank=True,
        choices=[(str(year), year) for year in range(timezone.localdate().year, 1900, -1)] + [DO_NOT_KNOW_CHOICE],
        verbose_name="Depuis quelle année ce régime de prévoyance est-il mis en œuvre dans l'ESAT ?  ",
    )

    # ESATStep.MOBILITY
    annual_transport_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel budget annuel avez-vous alloué au transport des travailleurs et travailleuses de leur domicile à l’ESAT (transport en commun et/ou navette et/ou taxi) en euro?",
    )
    nb_employee_transport = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont bénéficié d'un transport proposé par l'ESAT? (transport en commun et/ou navette et/ou taxi)",
    )
    nb_employee_mobility_inclusion = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Combien de travailleurs et travailleuses ont bénéficié de la carte mobilité inclusion?",
    )
    nb_employee_driving_licence = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Combien de travailleurs et travailleuses ont leur permis de conduire?"
    )
    nb_employee_code = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Combien de travailleurs et travailleuses ont le code?"
    )

    # ESATStep.VOUCHER
    holiday_voucher = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="L'ESAT propose-t-il des chèques vacances aux travailleurs et travailleuses?",
    )
    holiday_voucher_annual_budget = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel est le budget annuel de l'ESAT pour les chèques vacances ? (en euro)  ",
    )
    gift_voucher = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="L'ESAT propose-t-il des chèques cadeaux aux travailleurs et travailleuses ?",
    )
    gift_voucher_annual_budget = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Quel est le budget annuel de l'ESAT pour les chèques cadeaux ? (en euro) "
    )

    # ESATStep.CONVENTION
    rpe_convention_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Avez-vous signé en 2024 une convention de partenariat territoriale avec le réseau pour l’emploi ?",
    )
    pea_convention_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Avez-vous signé en 2024 une convention de partenariat avec une Plateforme Emploi Accompagné ?",
    )
    esat_pea_rattached = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Etes-vous un ESAT porteur ou rattaché à une structure qui gère une plateforme d’emploi accompagné (en tant que signataire de la convention de gestion)  ?",
    )
    ea_convention_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Avez-vous signé en 2024 une convention de partenariat avec une entreprise adaptée (EA)  ?",
    )
    nb_ea_convention_signed = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Avec combien d'entreprises adaptées présentes sur votre territoire avez-vous une convention de partenariat au 31 décembre 2024 ?",
    )

    # ESATStep.COUNSELORS
    nb_insertion_staff = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont dans vos effectifs ?",
        help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP.",
    )
    nb_insertion_dispo = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont mis à disposition ou mutualisés ?",
        help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP.",
    )

    # ESATStep.REVENUE
    annual_ca = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était votre chiffre d'affaire annuel commercial tout confondu (productions propres, prestations de service, mises à disposition de travailleurs et travailleuses auprès d’utilisateurs) ?",
        help_text="Entendre hors aide au poste de l’Etat au titre de la compensation de la rémunération garantie.",
    )
    annual_ca_production = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était votre chiffre d'affaire annuel commercial en productions propres ?",
    )
    annual_ca_service = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était votre chiffre d'affaire annuel commercial en prestation de service ?",
    )
    annual_ca_dispo = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel était votre chiffre d'affaire annuel commercial en mises à disposition de travailleurs et travailleuses auprès d’utilisateurs ?",
    )
    pct_ca_public = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(100)],
        verbose_name="Indiquez le pourcentage de votre chiffre d'affaires réalisé avec des clients du secteur public",
    )

    # ESATStep.SALES_BUDGET
    budget_commercial = models.CharField(
        null=True, blank=True, choices=BudgetState.choices, verbose_name="Sur le budget commercial, étiez-vous"
    )
    budget_commercial_deficit = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="De quel montant est ce déficit sur le budget commercial?",
    )
    budget_commercial_excedent = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="De quel montant est cet excédent sur le budget commercial?",
    )

    # ESATStep.SOCIAL_ACTIVITY_BUDGET
    budget_social = models.CharField(
        null=True,
        blank=True,
        choices=BudgetState.choices,
        verbose_name="Sur le budget principal de l'activité sociale, étiez-vous:",
        help_text="Il s’agit du résultat comptable de l'exercice",
    )
    budget_social_deficit = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="De quel montant est ce déficit sur le budget principal de l'activité sociale?",
    )
    budget_social_excedent = models.CharField(
        null=True,
        blank=True,
        choices=BudgetRange.choices,
        verbose_name="De quel montant est cet excédent sur le budget principal de l'activité sociale?",
    )
    budget_accessibility = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel a été le montant des investissements de mise aux normes de sécurité et d’accessibilité des installations réalisés par l'ESAT en 2024 ?",
    )
    budget_diversity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Quel a été le montant des investissements permettant de diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en 2024 ?",
        help_text="En lien le cas échéant avec le soutien de l’Etat via fonds d'intervention régional (FIR)",
    )

    # ESATStep.COMMENTS
    comments = models.TextField(
        null=True,
        blank=True,
        verbose_name="Nous arrivons à la fin du questionnaire - merci d'avoir pris le temps de le remplir.  Commentaires",
    )

    class Meta:
        verbose_name = "réponse ESAT"
        verbose_name_plural = "réponses ESAT"
