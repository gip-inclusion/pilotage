# ruff: noqa: E501
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import pilotage.itoutils.validators
import pilotage.surveys.models


class Migration(migrations.Migration):
    replaces = [
        ("surveys", "0001_initial"),
        ("surveys", "0002_add_esat_survey_and_answer"),
        ("surveys", "0003_survey_conclusion_survey_introduction"),
        ("surveys", "0004_esat_do_not_know_choice"),
        ("surveys", "0005_esat_min_max_validators"),
        ("surveys", "0006_alter_esatanswer_nb_insertion_dispo_and_more"),
        ("surveys", "0007_remove_answer_status"),
        ("surveys", "0008_survey_opening_period"),
        ("surveys", "0009_add_and_remove_esat_fields"),
        ("surveys", "0010_rename_fields"),
        ("surveys", "0011_update_help_texts"),
        ("surveys", "0012_new_partnership_agreement_fields"),
        ("surveys", "0013_new_feedbacks"),
        ("surveys", "0014_add_step_feedback"),
        ("surveys", "0015_survey_title"),
        ("surveys", "0016_update_fields_type_and_stuff"),
        ("surveys", "0017_update_fields_wordings"),
        ("surveys", "0018_update_support_themes_choices"),
        ("surveys", "0019_prefill_from_finess"),
        ("surveys", "0020_alter_answer_uid"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("kind", models.CharField(choices=[("ESAT", "ESAT")], verbose_name="type")),
                ("vintage", models.CharField(verbose_name="millésime")),
                ("name", models.SlugField(editable=False, unique=True, verbose_name="nom")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="créé le")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="mis à jour le")),
                ("conclusion", models.TextField(blank=True, null=True)),
                ("introduction", models.TextField(blank=True, null=True)),
                (
                    "opening_period",
                    django.contrib.postgres.fields.ranges.DateTimeRangeField(verbose_name="période d'ouverture"),
                ),
                ("title", models.CharField(blank=True, null=True, verbose_name="titre")),
            ],
            options={
                "verbose_name": "enquête",
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=pilotage.surveys.models.uuid7, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="créé le")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="mis à jour le")),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="surveys.survey",
                        verbose_name="enquête",
                    ),
                ),
            ],
            options={
                "verbose_name": "réponse",
            },
        ),
        migrations.CreateModel(
            name="ESATAnswer",
            fields=[
                (
                    "answer_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="surveys.answer",
                    ),
                ),
                (
                    "esat_role",
                    models.CharField(
                        blank=True, null=True, verbose_name="quelle est votre fonction au sein de l'ESAT ?"
                    ),
                ),
                ("esat_name", models.CharField(blank=True, null=True, verbose_name="quel est le nom de l’ESAT ?")),
                (
                    "esat_siret",
                    models.CharField(
                        blank=True,
                        max_length=14,
                        null=True,
                        validators=[pilotage.itoutils.validators.validate_siret],
                        verbose_name="quel est le numéro SIRET de l'ESAT ?",
                    ),
                ),
                (
                    "finess_num",
                    models.CharField(
                        blank=True,
                        max_length=9,
                        null=True,
                        validators=[pilotage.itoutils.validators.validate_finess],
                        verbose_name="quel est le numéro FINESS de l'établissement principal ?",
                    ),
                ),
                (
                    "esat_status",
                    models.CharField(
                        blank=True,
                        choices=[("PUBLIC", "Public"), ("NON_PROFIT", "Privé sans but lucratif")],
                        null=True,
                        verbose_name="quel est le statut de l'ESAT ?",
                    ),
                ),
                (
                    "esat_dept",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("01", "Ain"),
                            ("02", "Aisne"),
                            ("03", "Allier"),
                            ("04", "Alpes-de-Haute-Provence"),
                            ("05", "Hautes-Alpes"),
                            ("06", "Alpes-Maritimes"),
                            ("07", "Ardèche"),
                            ("08", "Ardennes"),
                            ("09", "Ariège"),
                            ("10", "Aube"),
                            ("11", "Aude"),
                            ("12", "Aveyron"),
                            ("13", "Bouches-du-Rhône"),
                            ("14", "Calvados"),
                            ("15", "Cantal"),
                            ("16", "Charente"),
                            ("17", "Charente-Maritime"),
                            ("18", "Cher"),
                            ("19", "Corrèze"),
                            ("2A", "Corse-du-Sud"),
                            ("2B", "Haute-Corse"),
                            ("21", "Côte-d'Or"),
                            ("22", "Côtes-d'Armor"),
                            ("23", "Creuse"),
                            ("24", "Dordogne"),
                            ("25", "Doubs"),
                            ("26", "Drôme"),
                            ("27", "Eure"),
                            ("28", "Eure-et-Loir"),
                            ("29", "Finistère"),
                            ("30", "Gard"),
                            ("31", "Haute-Garonne"),
                            ("32", "Gers"),
                            ("33", "Gironde"),
                            ("34", "Hérault"),
                            ("35", "Ille-et-Vilaine"),
                            ("36", "Indre"),
                            ("37", "Indre-et-Loire"),
                            ("38", "Isère"),
                            ("39", "Jura"),
                            ("40", "Landes"),
                            ("41", "Loir-et-Cher"),
                            ("42", "Loire"),
                            ("43", "Haute-Loire"),
                            ("44", "Loire-Atlantique"),
                            ("45", "Loiret"),
                            ("46", "Lot"),
                            ("47", "Lot-et-Garonne"),
                            ("48", "Lozère"),
                            ("49", "Maine-et-Loire"),
                            ("50", "Manche"),
                            ("51", "Marne"),
                            ("52", "Haute-Marne"),
                            ("53", "Mayenne"),
                            ("54", "Meurthe-et-Moselle"),
                            ("55", "Meuse"),
                            ("56", "Morbihan"),
                            ("57", "Moselle"),
                            ("58", "Nièvre"),
                            ("59", "Nord"),
                            ("60", "Oise"),
                            ("61", "Orne"),
                            ("62", "Pas-de-Calais"),
                            ("63", "Puy-de-Dôme"),
                            ("64", "Pyrénées-Atlantiques"),
                            ("65", "Hautes-Pyrénées"),
                            ("66", "Pyrénées-Orientales"),
                            ("67", "Bas-Rhin"),
                            ("68", "Haut-Rhin"),
                            ("69", "Rhône"),
                            ("70", "Haute-Saône"),
                            ("71", "Saône-et-Loire"),
                            ("72", "Sarthe"),
                            ("73", "Savoie"),
                            ("74", "Haute-Savoie"),
                            ("75", "Paris"),
                            ("76", "Seine-Maritime"),
                            ("77", "Seine-et-Marne"),
                            ("78", "Yvelines"),
                            ("79", "Deux-Sèvres"),
                            ("80", "Somme"),
                            ("81", "Tarn"),
                            ("82", "Tarn-et-Garonne"),
                            ("83", "Var"),
                            ("84", "Vaucluse"),
                            ("85", "Vendée"),
                            ("86", "Vienne"),
                            ("87", "Haute-Vienne"),
                            ("88", "Vosges"),
                            ("89", "Yonne"),
                            ("90", "Territoire de Belfort"),
                            ("91", "Essonne"),
                            ("92", "Hauts-de-Seine"),
                            ("93", "Seine-Saint-Denis"),
                            ("94", "Val-de-Marne"),
                            ("95", "Val-d'Oise"),
                            ("971", "Guadeloupe"),
                            ("972", "Martinique"),
                            ("973", "Guyane"),
                            ("974", "La Réunion"),
                            ("976", "Mayotte"),
                            ("975", "Saint-Pierre-et-Miquelon"),
                            ("977", "Saint-Barthélemy"),
                            ("978", "Saint-Martin"),
                            ("986", "Wallis-et-Futuna"),
                            ("987", "Polynésie française"),
                            ("988", "Nouvelle-Calédonie"),
                        ],
                        null=True,
                        verbose_name="quel est le département d'implantation de l'ESAT ?",
                    ),
                ),
                (
                    "pmsmp_refused",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous eu des refus de PMSMP par les organismes du réseau pour l'emploi (France Travail, Cap Emploi, Mission Locale) ?",
                    ),
                ),
                (
                    "prescription_delegate",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="êtes-vous délégataire de prescription de PMSMP ?"
                    ),
                ),
                (
                    "nb_worker_left",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs partis au cours de l'année n-1",
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses ont quitté l'ESAT ?",
                    ),
                ),
                (
                    "nb_worker_left_ea",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi en entreprise adaptée ?",
                    ),
                ),
                (
                    "nb_worker_left_asso",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé non lucratif (associations) ?",
                    ),
                ),
                (
                    "nb_worker_left_private",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé lucratif ?",
                    ),
                ),
                (
                    "nb_worker_left_public",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire public ?",
                    ),
                ),
                (
                    "nb_worker_half_time",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses étaient à temps partiel ?",
                    ),
                ),
                (
                    "nb_worker_cumul_esat_ea",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT et un emploi à temps partiel en Entreprise Adaptée ?",
                    ),
                ),
                (
                    "nb_worker_cumul_esat_mot",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT avec un emploi à temps partiel en milieu ordinaire classique, privé ou public ?",
                    ),
                ),
                (
                    "annual_ca",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était votre chiffre d'affaire annuel commercial tout confondu (productions propres, prestations de service, mises à disposition de travailleurs et travailleuses auprès d'utilisateurs) ?",
                    ),
                ),
                (
                    "annual_ca_mad",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était le montant annuel de votre chiffre d'affaires (Compte 706) issu exclusivement des contrats de mise à disposition de travailleurs et travailleuses handicapés (MAD) auprès d'utilisateurs tiers (entreprises, collectivités, associations) ?",
                    ),
                ),
                (
                    "annual_ca_production",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était votre chiffre d'affaire annuel commercial en productions propres ?",
                    ),
                ),
                (
                    "annual_ca_service",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était votre chiffre d'affaire annuel commercial en prestation de service ?",
                    ),
                ),
                (
                    "annual_transport_budget",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En euros",
                        null=True,
                        verbose_name="quel budget annuel avez-vous alloué au transport des travailleurs et travailleuses de leur domicile à l'ESAT (transport en commun et/ou navette et/ou taxi) ?",
                    ),
                ),
                (
                    "autodetermination_external_formation",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="la formation à l'autodétermination pour les travailleuses et travailleurs est-elle assurée par l'intermédiaire d'un organisme de formation ?",
                    ),
                ),
                (
                    "autodetermination_formation",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous mis en place une formation à l'autodétermination pour les travailleurs et travailleuses ?",
                    ),
                ),
                (
                    "budget_accessibility",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel a été le montant des investissements de mise aux normes de sécurité et d'accessibilité des installations réalisés par l'ESAT en n-1 ?",
                    ),
                ),
                (
                    "budget_commercial",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("SURPLUS", "excédentaire"),
                            ("BALANCE", "à l'équilibre"),
                            ("DEFICIT", "déficitaire"),
                        ],
                        null=True,
                        verbose_name="sur le résultat net de la SEC, étiez-vous",
                    ),
                ),
                (
                    "budget_commercial_deficit",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("LESS_THAN_100K", "Moins de 100 k€"),
                            ("RANGE_100K_500K", "100 k€ à 500k€"),
                            ("MORE_THAN_500K", "Plus de 500k€"),
                        ],
                        null=True,
                        verbose_name="de quel montant était ce déficit ?",
                    ),
                ),
                (
                    "budget_commercial_excedent",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("LESS_THAN_100K", "Moins de 100 k€"),
                            ("RANGE_100K_500K", "100 k€ à 500k€"),
                            ("MORE_THAN_500K", "Plus de 500k€"),
                        ],
                        null=True,
                        verbose_name="de quel montant était cet excédent?",
                    ),
                ),
                (
                    "budget_diversity",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel a été le montant des investissements pour diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en n-1 ?",
                    ),
                ),
                (
                    "budget_social",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("SURPLUS", "excédentaire"),
                            ("BALANCE", "à l'équilibre"),
                            ("DEFICIT", "déficitaire"),
                        ],
                        help_text="Budget de fonctionnement dit aussi budget social",
                        null=True,
                        verbose_name="sur le résultat de clôture de votre Budget de Fonctionnement (Section d'Exploitation du Budget Social), étiez-vous :",
                    ),
                ),
                (
                    "budget_social_deficit",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("LESS_THAN_100K", "Moins de 100 k€"),
                            ("RANGE_100K_500K", "100 k€ à 500k€"),
                            ("MORE_THAN_500K", "Plus de 500k€"),
                        ],
                        null=True,
                        verbose_name="de quel montant était ce déficit ?",
                    ),
                ),
                (
                    "budget_social_excedent",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("LESS_THAN_100K", "Moins de 100 k€"),
                            ("RANGE_100K_500K", "100 k€ à 500k€"),
                            ("MORE_THAN_500K", "Plus de 500k€"),
                        ],
                        null=True,
                        verbose_name="de quel montant était cet excédent?",
                    ),
                ),
                (
                    "contrib_opco",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="est-ce que l'ESAT a acquitté une contribution pour la formation des travailleurs et travailleuses auprès de l'OPCO Santé ou de l'OPCA ANFH (pour les ESAT publics) ?",
                    ),
                ),
                (
                    "cpf_unused_reason",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="pour quelles raisons les travailleurs et travailleurs n'utilisent pas leur CPF ?",
                    ),
                ),
                (
                    "documents_falclist",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("CONTRACT", "Oui : contrat d'accompagnement par le travail"),
                                ("BOOKLET", "Oui : livret d'accueil"),
                                ("REGULATION", "Oui : règlement de fonctionnement"),
                                ("NO", "Non"),
                            ]
                        ),
                        blank=True,
                        null=True,
                        verbose_name="au 31 décembre n-1, les principaux documents destinés aux travailleurs et travailleuses étaient-ils accessibles en FALC ou en communication alternative augmentée ? (contrat d'accompagnement par le travail, livret d'accueil, règlement de fonctionnement, etc.)",
                    ),
                ),
                (
                    "skills_notebook",
                    models.CharField(
                        blank=True,
                        choices=[("YES", "Oui"), ("NO", "Non"), ("WIP", "C'est en cours")],
                        null=True,
                        verbose_name="avez-vous mis en place un carnet de parcours et de compétences ?",
                    ),
                ),
                ("software_financial_help_type", models.TextField(blank=True, null=True, verbose_name="type d'aide")),
                (
                    "worker_delegate_formation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("TRAINING_ORGANIZATION", "Par l'intermédiaire d'un organisme de formation"),
                            ("INTERNALLY", "En interne"),
                            ("NO", "Non"),
                        ],
                        null=True,
                        verbose_name="est-ce que le délégué ou la déléguée a bénéficié d'une formation au cours de son mandat pour cette mission :",
                    ),
                ),
                (
                    "foresight_in_place",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="est-ce que l'ESAT a contribué en n-1 à un régime de prévoyance au sens de l'article R 243-9 du CASF, avec compensation par l'Etat d'une partie de la contribution ?",
                    ),
                ),
                (
                    "formation_cpf",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="quelle a été la formation majoritairement suivie par les travailleurs et travailleuses de l'ESAT au titre de leur CPF ?",
                    ),
                ),
                (
                    "formation_subject",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="quels ont été les sujets des formations dispensées, en interne, par l'ESAT ?",
                    ),
                ),
                (
                    "gift_voucher",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="l'ESAT propose-t-il des chèques cadeaux aux travailleurs et travailleuses ?",
                    ),
                ),
                (
                    "gift_voucher_annual_budget",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En euros",
                        null=True,
                        verbose_name="quel est le budget annuel de l'ESAT pour les chèques cadeaux ?",
                    ),
                ),
                (
                    "holiday_voucher",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="l'ESAT propose-t-il des chèques vacances aux travailleurs et travailleuses ?",
                    ),
                ),
                (
                    "holiday_voucher_annual_budget",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En euros",
                        null=True,
                        verbose_name="quel est le budget annuel de l'ESAT pour les chèques vacances ?",
                    ),
                ),
                (
                    "mean_worker_age",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="En nombre d'années",
                        max_digits=3,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(80),
                        ],
                        verbose_name="au 31 décembre n-1, quel était l'âge moyen des travailleurs et travailleuses accompagnés ?",
                    ),
                ),
                (
                    "mean_pct_esat_rem",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En % du SMIC",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="au 31 décembre n-1, quel était le % moyen de rémunération directe du travailleur pris en charge par l'ESAT ?",
                    ),
                ),
                (
                    "mean_seniority",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="En nombre d'années",
                        max_digits=3,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="au 31 décembre n-1, quelle était l'ancienneté moyenne des travailleurs et travailleuses accompagnés ?",
                    ),
                ),
                (
                    "mix_qvt_in_place",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, une instance mixte (salarié(e)s/travailleurs et travailleuses) sur la qualité de vie au travail (QVT), l'hygiène et la sécurité et l'évaluation des risques professionnels est-elle en place ?",
                    ),
                ),
                (
                    "nb_conv_exit_agreement",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de conventions d'appui sont en vigueur au 31 décembre n-1 dans l'ESAT avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d'un travailleur en milieu ordinaire ?",
                    ),
                ),
                (
                    "nb_delegate_hours",
                    models.BooleanField(blank=True, null=True, verbose_name="si oui, précisez le nombre d'heures"),
                ),
                (
                    "nb_worker_acc",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses avez-vous accompagnés ?",
                    ),
                ),
                (
                    "nb_worker_apprentice",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs sont en contrat d'apprentissage ?"
                    ),
                ),
                (
                    "nb_worker_autodetermination",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié dans l'année d'une formation à l'autodétermination ?",
                    ),
                ),
                (
                    "nb_worker_cdd",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs ont signé un CDD ?"
                    ),
                ),
                (
                    "nb_worker_cdi",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="pour les travailleurs et travailleuses ayant quitté l'ESAT pour un autre emploi, combien ont signé un CDI ?",
                    ),
                ),
                (
                    "nb_worker_code",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont le code ?",
                    ),
                ),
                (
                    "nb_worker_mad_indiv",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition individuelle ou collective chez employeur public ou privé ?",
                    ),
                ),
                (
                    "nb_worker_duoday",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont participé à Duoday ?",
                    ),
                ),
                (
                    "nb_worker_formation_opco",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs en file active",
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont suivi une formation prise en charge par l'OPCO Santé ou par l'ANFH ?",
                    ),
                ),
                (
                    "nb_worker_ft_job_seekers",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (effectif physique) en file active parmi ceux ayant acté dans leur projet leur volonté d'aller vers le milieu ordinaire de travail",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses se sont inscrits comme demandeurs d'emploi à France Travail ?",
                    ),
                ),
                (
                    "nb_worker_interim",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs sont en missions Interim ?"
                    ),
                ),
                (
                    "nb_worker_intern_formation",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'au moins une formation animée en interne par les salarié(e)s de l'ESAT ?",
                    ),
                ),
                (
                    "nb_worker_esrp",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont suivi une formation en établissement et service de réadaptation professionnelle (ESRP/ESPO/UEROS) ?",
                    ),
                ),
                (
                    "nb_worker_mispe_mdph",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de personnes (effectif physique) accueillies en n-1",
                        null=True,
                        verbose_name="combien de personnes ont été accompagnées par l'ESAT dans le cadre d'une mise en situation professionnelle (MISPE) prescrite par une MDPH ?",
                    ),
                ),
                (
                    "nb_worker_mispe_rpe",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de personnes (effectif physique) accueillies en n-1",
                        null=True,
                        verbose_name="combien de personnes ont été accompagnées par l'ESAT dans le cadre d'une mise en situation professionnelle (MISPE) prescrite par le réseau pour l'emploi (RPE) ?",
                    ),
                ),
                (
                    "nb_worker_mobility_inclusion_card",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié de la carte mobilité inclusion ?",
                    ),
                ),
                (
                    "nb_worker_new",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) parmi ceux admis en n-1",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses de l'ESAT ont été admis pour la première fois en milieu protégé de travail ?",
                    ),
                ),
                (
                    "nb_worker_previous_mot",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) parmi ceux admis en n-1",
                        null=True,
                        verbose_name="combien de travailleurs ont occupé un emploi en milieu ordinaire (y compris entreprise adaptée) antérieurement à leur admission dans l'ESAT ?",
                    ),
                ),
                (
                    "nb_worker_pmsmp",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont effectué une PMSMP ?",
                    ),
                ),
                (
                    "nb_worker_prof",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs sont en contrat de professionnalisation ?",
                    ),
                ),
                (
                    "nb_worker_rae_rsfp",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'une RAE ou d'une RSFP ?",
                    ),
                ),
                (
                    "nb_worker_reinteg",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses ayant réintégré l'ESAT",
                    ),
                ),
                (
                    "nb_worker_reinteg_other",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses ayant intégré un autre ESAT",
                    ),
                ),
                (
                    "nb_worker_with_public",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses ayant réalisé une activité dans un lieu au contact de la clientèle ?",
                    ),
                ),
                (
                    "nb_worker_vae",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'une VAE ?",
                    ),
                ),
                (
                    "nb_worker_service",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont réalisé une prestation de service auprès d'une entreprise, d'une collectivité publique ou de tout autre organisme ?",
                    ),
                ),
                (
                    "nb_worker_temporary",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) parmi ceux admis en n-1",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont été admis temporairement dans l'ESAT pour remplacer des travailleurs absents pour maladie, pour suivre une action formation ou pour occuper un emploi à temps partiel ?",
                    ),
                ),
                (
                    "nb_worker_transport",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="b. Combien de travailleurs et travailleuses ont bénéficié d'un transport financé ou organisé par l'ESAT ? (transport en commun et/ou navette et/ou taxi)",
                    ),
                ),
                (
                    "nb_worker_willing_mot",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs de l'ESAT ont exprimé dans leur projet personnalisé leur volonté d'aller travailler en milieu ordinaire ?",
                    ),
                ),
                (
                    "nb_employee_worked",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="En nombre de personnes",
                        max_digits=4,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="au 31 décembre n-1, combien de salariés ou d'agents publics (ESAT publics) étaient employés dans l'ESAT ?",
                    ),
                ),
                (
                    "nb_worker_worked_sunday",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses de l'ESAT ont travaillé au moins un dimanche ou un jour férié en n-1 ?",
                    ),
                ),
                (
                    "nb_worker_cpf_unused",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre de travailleurs (personnes physique) en file active parmi tous les travailleurs accompagnés en n-1",
                        null=True,
                        verbose_name="au 31 décembre n-1, et depuis leur admission dans l'ESAT, combien de travailleurs et travailleuses ont utilisé leur CPF ?",
                    ),
                ),
                (
                    "nb_worker_driving_licence",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont leur permis de conduire ?",
                    ),
                ),
                (
                    "nb_esat_agreement",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Nombre d'ESAT",
                        null=True,
                        verbose_name="avec combien d'ESAT avez-vous conventionné pour garantir l'exercice du droit au retour ?",
                    ),
                ),
                (
                    "nb_insertion_dispo",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="On parle ici de professionnels formés et exclusifs sur la mission d'inclusion. Répondre ici en ETP",
                        max_digits=4,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="au 31 décembre n-1, combien de postes de conseillers en parcours d'insertion ou assimilé étaient mis à disposition ou mutualisés ?",
                    ),
                ),
                (
                    "nb_insertion_staff",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="On parle ici de professionnels formés et exclusifs sur la mission d'inclusion. Répondre ici en ETP",
                        max_digits=4,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="au 31 décembre n-1, combien de conseillers en parcours d'insertion ou assimilé étaient dans vos effectifs ?",
                    ),
                ),
                (
                    "nb_places_allowed",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=4,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="au 31 décembre n-1, quel était l'agrément fixé par l'ARS pour l'ESAT en nombre de places autorisées ?",
                    ),
                ),
                (
                    "nb_support_hours",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("LESS_THAN_50", "Moins de 50 heures"),
                            ("RANGE_100_150", "Entre 100 et 150 heures"),
                            ("RANGE_150_200", "Entre 150 et 200 heures"),
                            ("RANGE_200_250", "Entre 200 et 250 heures"),
                            ("MORE_THAN_250", "Plus de 250 heures"),
                            ("UNKNOWN", "Inconnu, non quantifiable"),
                        ],
                        help_text="Nombre d'heures en moyenne par travailleur sur année n-1",
                        null=True,
                        verbose_name="quel était le nombre d'heures de soutien liées à l'activité professionnelle, dont en moyenne chaque travailleur a bénéficié (rémunérées et comprises dans le temps de travail) ?",
                    ),
                ),
                (
                    "retirement_preparation_nb_workers",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'actions de préparation à la retraite ?",
                    ),
                ),
                (
                    "opco_or_anfh_refusal",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="l'ESAT a –t-il fait l'objet d'un ou plusieurs refus de financement d'une formation par l'OPCO Santé ou l'ANFH ?",
                    ),
                ),
                (
                    "pct_ca_public",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="indiquez le pourcentage de votre chiffre d'affaires réalisé avec des clients du secteur public",
                    ),
                ),
                (
                    "pct_more_than50",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="combien de travailleurs ou travailleuses de plus de 50 ans ont travaillé dans l'ESAT en n-1 ?",
                    ),
                ),
                (
                    "pct_opco",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En %",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="quel a été le taux de votre contribution à l'OPCO Santé ou à l'ANFH ?",
                    ),
                ),
                (
                    "profit_sharing_bonus",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En euros. Possibilité de mettre 0.",
                        null=True,
                        verbose_name="en n-1, quel était le montant moyen de la prime d'intéressement (au sens de l'article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
                    ),
                ),
                (
                    "retirement_preparation_actions",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                (
                                    "ADMINISTRATIVE_ASSISTANCE",
                                    "Accompagnement administratif (rendez-vous avec la CARSAT, aide à la préparation du dossier, informations sur les droits, etc.)",
                                ),
                                ("UAAT", "Session de sensibilisation ou formation sur les droits à la retraite"),
                                (
                                    "MEETING_SCHEDULED",
                                    "Organisation d'un RDV avec un professionnel compétent sur le sujet (Assistante sociale, RH, Directeur/-trice, etc.)",
                                ),
                                ("PERSONAL_PLAN", "Inscription dans le projet de la personne"),
                                ("CAF", "Simulation de ressources auprès des services de la CAF"),
                                (
                                    "WORKING_HOURS_REDUCTION_AND_ORGANISATION",
                                    "Aménagement / réduction du temps de travail",
                                ),
                                (
                                    "PSYCHOLOGICAL_AND_SOCIAL_ASSISTANCE",
                                    "Actions de transition psychologique et sociale",
                                ),
                                ("OTHER", "Autres"),
                            ]
                        ),
                        blank=True,
                        null=True,
                        verbose_name="quelles ont été les actions conduites par l'ESAT pour préparer les travailleurs et travailleuses au départ à la retraite ?",
                    ),
                ),
                (
                    "support_themes",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("WORKSHOP_JOB_SEARCH", "Atelier d'accompagnement à la recherche d'emploi"),
                                ("WORKSHOP_WELLBEING", "Atelier de prévention santé / bien-être au travail"),
                                ("PROFESSIONAL_SUPPORT", "Activité de soutien au parcours professionnel"),
                                ("CPF_OPENED", "Ouverture du Compte Professionnel de Formation"),
                                ("COMPANY_TOUR", "Visites dans les entreprises"),
                                ("PREMISES_TOUR", "Visites des locaux de l’ESAT par les entreprises"),
                                ("OTHER", "Autres"),
                            ]
                        ),
                        blank=True,
                        null=True,
                        verbose_name="sur quelles thématiques principales ?",
                    ),
                ),
                (
                    "uaat_inscription",
                    models.CharField(
                        blank=True,
                        choices=[("YES", "Oui"), ("NO", "Non"), ("WIP", "C'est en cours")],
                        null=True,
                        verbose_name="êtes-vous inscrit dans la démarche Un Avenir Après le Travail (UAAT) ?",
                    ),
                ),
                (
                    "year_foresight_in_place",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("2026", 2026),
                            ("2025", 2025),
                            ("2024", 2024),
                            ("2023", 2023),
                            ("2022", 2022),
                            ("2021", 2021),
                            ("2020", 2020),
                            ("2019", 2019),
                            ("2018", 2018),
                            ("2017", 2017),
                            ("2016", 2016),
                            ("2015", 2015),
                            ("2014", 2014),
                            ("2013", 2013),
                            ("2012", 2012),
                            ("2011", 2011),
                            ("2010", 2010),
                            ("2009", 2009),
                            ("2008", 2008),
                            ("2007", 2007),
                            ("2006", 2006),
                            ("2005", 2005),
                            ("2004", 2004),
                            ("2003", 2003),
                            ("2002", 2002),
                            ("2001", 2001),
                            ("2000", 2000),
                            ("1999", 1999),
                            ("1998", 1998),
                            ("1997", 1997),
                            ("1996", 1996),
                            ("1995", 1995),
                            ("1994", 1994),
                            ("1993", 1993),
                            ("1992", 1992),
                            ("1991", 1991),
                            ("1990", 1990),
                            ("1989", 1989),
                            ("1988", 1988),
                            ("1987", 1987),
                            ("1986", 1986),
                            ("1985", 1985),
                            ("1984", 1984),
                            ("1983", 1983),
                            ("1982", 1982),
                            ("1981", 1981),
                            ("1980", 1980),
                            ("1979", 1979),
                            ("1978", 1978),
                            ("1977", 1977),
                            ("1976", 1976),
                            ("1975", 1975),
                            ("1974", 1974),
                            ("1973", 1973),
                            ("1972", 1972),
                            ("1971", 1971),
                            ("1970", 1970),
                            ("1969", 1969),
                            ("1968", 1968),
                            ("1967", 1967),
                            ("1966", 1966),
                            ("1965", 1965),
                            ("1964", 1964),
                            ("1963", 1963),
                            ("1962", 1962),
                            ("1961", 1961),
                            ("1960", 1960),
                            ("1959", 1959),
                            ("1958", 1958),
                            ("1957", 1957),
                            ("1956", 1956),
                            ("1955", 1955),
                            ("1954", 1954),
                            ("1953", 1953),
                            ("1952", 1952),
                            ("1951", 1951),
                            ("1950", 1950),
                            ("1949", 1949),
                            ("1948", 1948),
                            ("1947", 1947),
                            ("1946", 1946),
                            ("1945", 1945),
                            ("1944", 1944),
                            ("1943", 1943),
                            ("1942", 1942),
                            ("1941", 1941),
                            ("1940", 1940),
                            ("1939", 1939),
                            ("1938", 1938),
                            ("1937", 1937),
                            ("1936", 1936),
                            ("1935", 1935),
                            ("1934", 1934),
                            ("1933", 1933),
                            ("1932", 1932),
                            ("1931", 1931),
                            ("1930", 1930),
                            ("1929", 1929),
                            ("1928", 1928),
                            ("1927", 1927),
                            ("1926", 1926),
                            ("1925", 1925),
                            ("1924", 1924),
                            ("1923", 1923),
                            ("1922", 1922),
                            ("1921", 1921),
                            ("1920", 1920),
                            ("1919", 1919),
                            ("1918", 1918),
                            ("1917", 1917),
                            ("1916", 1916),
                            ("1915", 1915),
                            ("1914", 1914),
                            ("1913", 1913),
                            ("1912", 1912),
                            ("1911", 1911),
                            ("1910", 1910),
                            ("1909", 1909),
                            ("1908", 1908),
                            ("1907", 1907),
                            ("1906", 1906),
                            ("1905", 1905),
                            ("1904", 1904),
                            ("1903", 1903),
                            ("1902", 1902),
                            ("1901", 1901),
                            ("DO_NOT_KNOW", "Je ne sais pas"),
                        ],
                        null=True,
                        verbose_name="depuis quelle année ce régime de prévoyance est-il mis en œuvre dans l'ESAT ?",
                    ),
                ),
                (
                    "comments",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="nous arrivons à la fin du questionnaire. Ce champ libre vous permet d'apporter toute précision complémentaire ou de clarifier certaines informations si nécessaire. Merci de faire référence aux questions en utilisant leur identifiant (exemple : Rubrique “Aide à la mobilité”, Question c), la donnée n'est pas disponible car nous n'avons pas l'information pour 2 des 5 travailleurs concernés.)",
                    ),
                ),
                (
                    "insertion_staff_funding",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("BPAS", "Par votre budget de fonctionnement (BPAS)"),
                                ("BAPC", "Par votre budget annexe de production et de commercialisation (BAPC)"),
                                ("OTHER", "Autres"),
                            ]
                        ),
                        blank=True,
                        null=True,
                        verbose_name="comment sont-ils financés ?",
                    ),
                ),
                (
                    "nb_conv_exit_agreement_new",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de conventions d'appui ont été signées dans l'année n-1 avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d'un travailleur en milieu ordinaire ?",
                    ),
                ),
                (
                    "nb_employee_reverse_duoday",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, combien de professionnels du milieu ordinaire ont participé à des Duoday inversés ?",
                    ),
                ),
                (
                    "nb_worker_left_other_reason",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien ont quitté l'ESAT pour d'autres raisons ?"
                    ),
                ),
                (
                    "nb_worker_only_inside",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En nombre de travailleurs (effectif physique) en file active",
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses étant resté travailler dans les murs sans contact avec le public ou le milieu ordinaire de travail ?",
                    ),
                ),
                (
                    "skills_validation_type",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("RAE", "Reconnaissance des acquis de l'expérience (RAE)"),
                                ("RSFP", "Reconnaissance des savoir-faire professionnels (RSFP)"),
                                ("VAE", "Validation des acquis de l'expérience (VAE)"),
                                ("AFEST", "Action de formation en situation de travail (AFEST)"),
                                ("OTHER", "Autres"),
                                ("NONE", "Aucune"),
                            ]
                        ),
                        blank=True,
                        null=True,
                        verbose_name="quels ont été les types de dispositifs dont ont bénéficié les travailleurs et travailleuses de l'ESAT pour reconnaitre et développer leurs compétences ?",
                    ),
                ),
                (
                    "agreement_signed_dept_pae",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="pour l'année n-1, une convention était-elle en vigueur avec la plateforme “emploi accompagné” du département ?",
                    ),
                ),
                (
                    "agreement_signed_ea",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="pour l'année n-1, une convention était-elle en vigueur avec une Entreprise adaptée ?",
                    ),
                ),
                (
                    "agreement_signed_ft",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="pour l'année n-1, une convention était-elle en vigueur avec les acteurs du réseau pour l’emploi (France Travail, Cap Emploi et Mission locale) ?",
                    ),
                ),
                (
                    "worker_delegate",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, y-a-t-il dans l'ESAT un.e délégué.e des travailleurs élu.e ?",
                    ),
                ),
                (
                    "worker_delegate_hours_credit",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, est-ce que le délégué a bénéficié d'un crédit d'heures chaque mois pour remplir sa mission ?",
                    ),
                ),
                ("step_feedback", models.JSONField(blank=True, default=dict, null=True)),
                (
                    "nb_employee_shared",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="En nombre de personnes",
                        max_digits=4,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="parmi eux, combien étaient mutualisés sur plusieurs ESAT ?",
                    ),
                ),
                (
                    "after_skills_validation",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="parmi les travailleurs sortis dans l’année, combien avaient obtenu une validation ou une reconnaissance de leurs compétences en amont ?",
                    ),
                ),
                (
                    "software_financial_help",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("CNR", "Les Crédits Non Reconductibles"),
                                ("FATESAT", "Le FATESAT"),
                                ("CCAH", "Fonds CCAH (Comité National de Coordination Action Handicap)"),
                                ("DEDICATED_FUNDING", "Fonds spécifiques type AGGIRC-ARCO"),
                                ("OTHER", "Autres"),
                            ]
                        ),
                        blank=True,
                        null=True,
                        verbose_name="l'ESAT a t-il bénéficié d'une aide financière pour mettre en place ce carnet et le cas échéant, acquérir un logiciel ?",
                    ),
                ),
                (
                    "managing_organization_finess",
                    models.CharField(
                        blank=True,
                        max_length=9,
                        null=True,
                        validators=[pilotage.itoutils.validators.validate_finess],
                        verbose_name="quel est le numéro FINESS de l’entité juridique de rattachement ?",
                    ),
                ),
            ],
            options={
                "verbose_name": "réponse ESAT",
                "verbose_name_plural": "réponses ESAT",
            },
            bases=("surveys.answer",),
        ),
    ]
