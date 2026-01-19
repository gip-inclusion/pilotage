# ruff: noqa: E501
import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import pilotage.itoutils.validators


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="survey",
            name="kind",
            field=models.CharField(choices=[("ESAT", "ESAT")], verbose_name="type"),
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
                ("esat_name", models.CharField(blank=True, null=True, verbose_name="quel est le nom de votre ESAT ?")),
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
                        verbose_name="quel est le numéro FINESS de l’établissement principal ?",
                    ),
                ),
                (
                    "managing_organization_name",
                    models.CharField(blank=True, null=True, verbose_name="quel est votre organisme gestionnaire ?"),
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
                        verbose_name="quel est le département d’implantation de l'ESAT ?",
                    ),
                ),
                (
                    "pmsmp_refused",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous eu des refus de PMSMP par les organismes du réseau pour l'emploi (France Travail, Cap Emploi, Mission Locale) pour un ou plusieurs de vos travailleurs et travailleuses ?",
                    ),
                ),
                (
                    "prescription_delegate",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="êtes-vous délégataire de prescription de PMSMP pour les travailleurs et travailleuses que vous accompagnez ?",
                    ),
                ),
                (
                    "nb_employee_left",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses ont quitté l'ESAT ?",
                    ),
                ),
                (
                    "nb_employee_left_ea",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi en entreprise adaptée ?",
                    ),
                ),
                (
                    "nb_employee_left_asso",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé non lucratif (associations) ?",
                    ),
                ),
                (
                    "nb_employee_left_private",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé lucratif ?",
                    ),
                ),
                (
                    "nb_employee_left_public",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire public ?",
                    ),
                ),
                (
                    "nb_employee_half_time",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="hors situation de temps partagé entre milieu protégé et milieu ordinaire",
                        null=True,
                        verbose_name="parmi eux, combien de travailleurs et travailleuses étaient à temps partiel ?",
                    ),
                ),
                (
                    "pct_activity_outside",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("0-20", "De 0% à 20%"),
                            ("21-40", "De 21% à 40%"),
                            ("41-60", "De 41% à 60%"),
                            ("61-80", "De 61% à 80%"),
                            ("81-100", "De 81 à 100%"),
                        ],
                        null=True,
                        verbose_name="sur l’ensemble de l’activité de l’ESAT, quel est le pourcentage d’activité exercée en dehors de l’établissement ?",
                    ),
                ),
                (
                    "nb_employee_cumul_esat_ea",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Ici, il ne faut pas comptabiliser par contrat mais par travailleur",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT et un emploi à temps partiel en Entreprise Adaptée ?",
                    ),
                ),
                (
                    "nb_employee_cumul_esat_ordi",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Ici, il ne faut pas comptabiliser par contrat mais par travailleur",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT avec un emploi à temps partiel en milieu ordinaire classique, privé ou public ?",
                    ),
                ),
                (
                    "after_reco_situation_list",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NO_CHANGES", "Maintien sur l’activité professionnelle initiale au sein de l'ESAT"),
                            ("OTHER_ACTIVITY", "Accès à d’autres activités professionnelles au sein de l'ESAT"),
                            ("OTHER_ESAT", "Changement d’ESAT"),
                            (
                                "ESRP",
                                "Accès à une formation via un établissement ou service de réadaptation professionnelle (ESRP)",
                            ),
                            ("TRAINING_COURSE", "Accès à une formation via un organisme de formation"),
                            ("PARTIAL_TIME_WORK", "Accès à un emploi via le temps partagé"),
                            ("LEFT", "Sortie de l'ESAT pour accéder à un emploi en milieu ordinaire ou adapté"),
                        ],
                        null=True,
                        verbose_name="a l’issue de cette reconnaissance ou validation, quelle a été la suite du parcours des travailleurs et travailleuses concerné(e)s ?",
                    ),
                ),
                (
                    "annual_ca",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Entendre hors aide au poste de l’Etat au titre de la compensation de la rémunération garantie.",
                        null=True,
                        verbose_name="quel était votre chiffre d'affaire annuel commercial tout confondu (productions propres, prestations de service, mises à disposition de travailleurs et travailleuses auprès d’utilisateurs) ?",
                    ),
                ),
                (
                    "annual_ca_dispo",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel est le montant annuel de votre chiffre d'affaires (Compte 706) issu exclusivement des contrats de mise à disposition de travailleurs et travailleuses handicapés (MAD) auprès d'utilisateurs tiers (entreprises, collectivités, associations) ?",
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
                    "annual_health_complementary_budget",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était le montant annuel pour l'année n-1 pour l'ensemble des travailleurs et travailleuses couverts de la contribution acquittée par l’ESAT ?",
                    ),
                ),
                (
                    "annual_transport_budget",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel budget annuel avez-vous alloué au transport des travailleurs et travailleuses de leur domicile à l’ESAT (transport en commun et/ou navette et/ou taxi) ?",
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
                        verbose_name="quel a été le montant des investissements de mise aux normes de sécurité et d’accessibilité des installations réalisés par l'ESAT en n-1 ?",
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
                        verbose_name="de quel montant est-ce déficit ?",
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
                        verbose_name="de quel montant est-cet excédant?",
                    ),
                ),
                (
                    "budget_diversity",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="En lien le cas échéant avec le soutien de l’Etat via fonds d'intervention régional (FIR)",
                        null=True,
                        verbose_name="quel a été le montant des investissements permettant de diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en n-1 ?",
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
                        help_text="Il s’agit du résultat comptable de l'exercice",
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
                        verbose_name="de quel montant est-ce déficit ?",
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
                        verbose_name="de quel montant est-cet excédant?",
                    ),
                ),
                (
                    "contrib_opco",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="est-ce que l'ESAT a acquitté une contribution pour la formation des travailleurs et travailleuses auprès de l’OPCO Santé ou de l’OPCA ANFH (pour les ESAT publics) ?",
                    ),
                ),
                (
                    "cpfreason",
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
                        help_text="Le facile à lire et à comprendre (FALC) est une méthode qui a pour but de traduire un langage classique en un langage simplifié.",
                        null=True,
                        size=None,
                        verbose_name="au 31 décembre n-1, les principaux documents destinés aux travailleurs et travailleuses étaient-ils accessibles en FALC ou en communication alternative augmentée?(contrat d’accompagnement par le travail, livret d’accueil, règlement de fonctionnement, etc.)  ",
                    ),
                ),
                (
                    "duoday_board",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous mis en place un carnet de parcours et de compétences ?",
                    ),
                ),
                ("duoday_financial_help_type", models.TextField(blank=True, null=True, verbose_name="type d'aide")),
                (
                    "duoday_software_financial_help",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="l'ESAT a t-il bénéficié d’une aide financière pour mettre en place ce carnet et le cas échéant, acquérir un logiciel ?",
                    ),
                ),
                (
                    "duoday_software_used",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous utilisé un logiciel spécifique pour mettre en place le carnet, et si oui lequel ?",
                    ),
                ),
                (
                    "ea_convention_signed",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous signé en n-1 une convention de partenariat avec une entreprise adaptée (EA)  ?",
                    ),
                ),
                (
                    "employee_delegate",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, y-a-t-il dans l'ESAT un délégué/une déléguée des travailleurs élu(e) ?",
                    ),
                ),
                (
                    "employee_delegate_formation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("TRAINING_ORGANIZATION", "Par l'intermédiaire d'un organisme de formation"),
                            ("INTERNALLY", "En interne"),
                        ],
                        null=True,
                        verbose_name="est-ce que le délégué ou la déléguée a bénéficié d'une formation au cours de son mandat pour cette mission :",
                    ),
                ),
                (
                    "employee_delegate_hours_credit",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="est-ce que le délégué ou la déléguée bénéficie d'un crédit d'heures chaque mois pour remplir sa mission ?",
                    ),
                ),
                (
                    "esat_pea_rattached",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="êtes-vous un ESAT porteur ou rattaché à une structure qui gère une plateforme d’emploi accompagné (en tant que signataire de la convention de gestion)  ?",
                    ),
                ),
                (
                    "foresight_in_place",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="est-ce que l'ESAT a contribué en n-1 à un régime de prévoyance au sens de l’article R 243-9 du CASF, avec compensation par l’Etat d’une partie de la contribution ?",
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
                        verbose_name="quels ont été les sujets des formation dispensés par l’ESAT ?",
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
                        null=True,
                        verbose_name="quel est le budget annuel de l'ESAT pour les chèques cadeaux ?",
                    ),
                ),
                (
                    "health_complementary",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="les travailleurs et travailleuses de l’ESAT bénéficiaient-ils en n-1 d’une complémentaire santé collective avec prise en charge par l’ESAT d’une partie du coût de la cotisation ?",
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
                        null=True,
                        verbose_name="quel est le budget annuel de l'ESAT pour les chèques vacances ?",
                    ),
                ),
                (
                    "mean_employee_age",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=3,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(80)],
                        verbose_name="au 31 décembre n-1, quel était l’âge moyen des travailleurs et travailleuses accompagnés ?",
                    ),
                ),
                (
                    "mean_pct_esat_rem",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="au 31 décembre n-1, quel était le montant moyen de la part rémunération garantie du travailleur prise en charge financièrement par l'ESAT ?",
                    ),
                ),
                (
                    "mean_seniority",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        help_text="L'ancienneté moyenne doit être exprimée en mois",
                        max_digits=3,
                        null=True,
                        verbose_name="au 31 décembre n-1, quelle était l’ancienneté moyenne des travailleurs et travailleuses accompagnés ?",
                    ),
                ),
                (
                    "mix_qvt_in_place",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="une instance mixte (salarié(e)s/travailleurs et travailleuses) sur la qualité de vie au travail (QVT), l’hygiène et la sécurité et l’évaluation des risques professionnels est-elle en place en année n-1 ?",
                    ),
                ),
                (
                    "nb_conv_exit",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de conventions d'appui sont actuellement en vigueur dans l'ESAT avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d’un travailleur en milieu ordinaire au 31/12/n-1 ?",
                    ),
                ),
                (
                    "nb_delegate_hours",
                    models.BooleanField(blank=True, null=True, verbose_name="si oui, précisez le nombre d'heures"),
                ),
                (
                    "nb_ea_convention_signed",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avec combien d'entreprises adaptées présentes sur votre territoire avez-vous une convention de partenariat au 31 décembre n-1 ?",
                    ),
                ),
                (
                    "nb_employee_acc",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses avez-vous accompagné ?",
                    ),
                ),
                (
                    "nb_employee_apprentice",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs sont en contrat d'apprentissage ?"
                    ),
                ),
                (
                    "nb_employee_autodetermination",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié dans l'année d’une formation à l’autodétermination ?",
                    ),
                ),
                (
                    "nb_employee_cdd",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs ont signé un CDD ?"
                    ),
                ),
                (
                    "nb_employee_cdi",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="pour les travailleurs et travailleuses ayant quitté l'ESAT pour un autre emploi, combien ont signé un CDI ?",
                    ),
                ),
                (
                    "nb_employee_code",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs et travailleuses ont le code ?"
                    ),
                ),
                (
                    "nb_employee_dispo_collec",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition collective d'un employeur public ou privé ?",
                    ),
                ),
                (
                    "nb_employee_dispo_indiv",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition individuelle d'un employeur public ou privé ?",
                    ),
                ),
                (
                    "nb_employee_duoday",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont participé à Duoday ?",
                    ),
                ),
                (
                    "nb_employee_formation_opco",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont suivi une formation prise en charge par l'OPCO Santé ou par l’ANFH ?",
                    ),
                ),
                (
                    "nb_employee_ft_job_seekers",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses se sont inscrits comme demandeurs d’emploi à France Travail ?",
                    ),
                ),
                (
                    "nb_employee_interim",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="combien de travailleurs sont en missions Interim ?"
                    ),
                ),
                (
                    "nb_employee_intern_formation",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'au moins une formation animée en interne par les salarié(e)s de l'ESAT ?",
                    ),
                ),
                (
                    "nb_employee_left_esrp",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont suivi une formation en établissement et service de réadaptation professionnelle (ESRP) ?",
                    ),
                ),
                (
                    "nb_employee_mispe_mdph",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par une MDPH ?",
                    ),
                ),
                (
                    "nb_employee_mispe_rpe",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par le réseau pour l'emploi (RPE) ?",
                    ),
                ),
                (
                    "nb_employee_mobility_inclusion",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié de la carte mobilité inclusion ?",
                    ),
                ),
                (
                    "nb_employee_new",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était le nombre de travailleurs et travailleuses dans l'ESAT admis pour la première fois en milieu protégé de travail ?",
                    ),
                ),
                (
                    "nb_employee_ordinary_job",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était le nombre de travailleurs et travailleuses dans l'ESAT ayant occupé antérieurement à leur admission un emploi en milieu ordinaire (y compris entreprise adapté) ?",
                    ),
                ),
                (
                    "nb_employee_pmsmp",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont effectué une PMSMP ?",
                    ),
                ),
                (
                    "nb_employee_prof",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs sont en contrat de professionnalisation ?",
                    ),
                ),
                (
                    "nb_employee_rae",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d’une RAE ou d’une RSFP ?",
                    ),
                ),
                (
                    "nb_employee_reinteg",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses ayant réintégré l'ESAT",
                    ),
                ),
                (
                    "nb_employee_reinteg_other",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses ayant intégré un autre ESAT",
                    ),
                ),
                (
                    "nb_employee_restau",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="nombre de travailleurs et travailleuses ayant réalisé une activité dans un lieu au contact de la clientèle ?",
                    ),
                ),
                (
                    "nb_employee_rsfp",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d’une VAE ?",
                    ),
                ),
                (
                    "nb_employee_service",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont réalisé une prestation de service auprès d'une entreprise, d'une collectivité publique ou de tout autre organisme, assurée avec ou un plusieurs salarié(e)s de l'ESAT ?",
                    ),
                ),
                (
                    "nb_employee_temporary",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="et maintenir ainsi votre capacité d’activité en bénéficiant via l’ASP de l’annualisation de l’aide au poste",
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont été admis temporairement dans l'ESAT pour remplacer des travailleurs absents pour maladie, pour suivre une action formation ou pour occuper un emploi à temps partiel ?",
                    ),
                ),
                (
                    "nb_employee_transport",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d'un transport proposé par l'ESAT? (transport en commun et/ou navette et/ou taxi)",
                    ),
                ),
                (
                    "nb_employee_willing_ordinary",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs de l'ESAT ont exprimé dans leur projet personnalisé leur volonté d’aller travailler en milieu ordinaire ?",
                    ),
                ),
                (
                    "nb_employee_worked",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=4,
                        null=True,
                        verbose_name="Combien de salarié(e)s ou d’agents publics (ESAT publics) ont été employés dans l'ESAT ?",
                    ),
                ),
                (
                    "nb_employee_worked_sunday",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses de l'ESAT ont travaillé au moins un dimanche ou un jour férié en n-1 ?",
                    ),
                ),
                (
                    "nb_employeed_cpf_unused",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="au 31 décembre n-1, et depuis leur admission dans l'ESAT, combien de travailleurs et travailleuses ont utilisé leur CPF ?",
                    ),
                ),
                (
                    "nb_employee_driving_licence",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont leur permis de conduire ?",
                    ),
                ),
                (
                    "nb_esat_conv",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="avec combien d'ESAT avez-vous conventionné pour garantir l’exercice du droit au retour ?",
                    ),
                ),
                (
                    "nb_insertion_dispo",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP.",
                        null=True,
                        verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont mis à disposition ou mutualisés ?",
                    ),
                ),
                (
                    "nb_insertion_staff",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP.",
                        null=True,
                        verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont dans vos effectifs ?",
                    ),
                ),
                (
                    "nb_places_allowed",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=4,
                        null=True,
                        verbose_name="au 31 décembre n-1, quel était l'agrément fixé par l'ARS pour l'ESAT en nombre de places autorisées ?",
                    ),
                ),
                (
                    "nb_support_hours",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="quel était le nombre d’heures de soutien liées à l’activité professionnelle, dont en moyenne chaque travailleur a bénéficié (rémunérées et comprises dans le temps de travail) ?",
                    ),
                ),
                (
                    "nb_uaat_beneficiary",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="combien de travailleurs et travailleuses ont bénéficié d’actions de préparation à la retraite, dans le cadre ou non d’Un Avenir Après le Travail ?",
                    ),
                ),
                (
                    "opco_or_anfh_refusal",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="l'ESAT a –t-il fait l’objet d’un ou plusieurs refus de financement d’une formation par l’OPCO Santé ou l’ANFH ?",
                    ),
                ),
                (
                    "pct_ca_public",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="indiquez le pourcentage de votre chiffre d'affaires réalisé avec des clients du secteur public",
                    ),
                ),
                (
                    "pct_employee_activity_bonus",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="quel pourcentage de travailleurs et travailleuses bénéficie de la prime d'activité?",
                    ),
                ),
                (
                    "pct_health_complementary_esat",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Possibilité de mettre 0",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="quel était le pourcentage de financement par l'ESAT en n-1 ?",
                    ),
                ),
                (
                    "pct_more_than50",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="combien de travailleurs ou travailleuses de plus de 50 ans ont travaillé dans l’ESAT en n-1 ?",
                    ),
                ),
                (
                    "pct_opco",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="En pourcentage de l’assiette de contribution",
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="quel a été le taux de votre contribution à l’OPCO Santé ou à l’ANFH ?",
                    ),
                ),
                (
                    "pea_convention_signed",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous signé en n-1 une convention de partenariat avec une Plateforme Emploi Accompagné ?",
                    ),
                ),
                (
                    "profit_sharing_bonus",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Possibilité de mettre 0",
                        null=True,
                        verbose_name="en n-1, quel était le montant moyen de la prime d’intéressement (au sens de l’article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
                    ),
                ),
                (
                    "retirement_preparation",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="quelles ont été les actions conduites par l'ESAT pour préparer les travailleurs et travailleuses au départ à la retraite (inscription dans la démarche Un Avenir Après le Travail, rendez-vous organisés avec la CARSAT, etc.) ?",
                    ),
                ),
                (
                    "rpe_convention_signed",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name="avez-vous signé en n-1 une convention de partenariat territoriale avec le réseau pour l’emploi ?",
                    ),
                ),
                (
                    "support_themes",
                    models.TextField(blank=True, null=True, verbose_name="sur quelles thématiques principales ?"),
                ),
                (
                    "uaat_inscription",
                    models.CharField(
                        blank=True,
                        choices=[("YES", "Oui"), ("NO", "Non"), ("IN_PROGRESS", "C'est en cours")],
                        null=True,
                        verbose_name="Êtes-vous inscrit dans la démarche Un Avenir Après le Travail (UAAT) ?",
                    ),
                ),
                (
                    "year_foresight_in_place",
                    models.CharField(
                        blank=True,
                        choices=[
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
                        verbose_name="nous arrivons à la fin du questionnaire. Ce champ libre vous permet d’apporter toute précision complémentaire, d’exprimer un doute concernant vos réponses ou de clarifier certaines informations si nécessaire. Merci de faire référence aux questions en utilisant leur identifiant (exemple : Rubrique “Aide à la mobilité”, Question 1), la donnée n’est pas disponible car nous n’avons pas l’information pour 2 des 5 travailleurs concernés.)",
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
