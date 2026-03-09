# ruff: noqa: E501
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0016_update_fields_type_and_stuff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="after_skills_validation",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="parmi les travailleurs sortis dans l’année, combien avaient obtenu une validation ou une reconnaissance de leurs compétences en amont ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="agreement_signed_dept_pae",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec la plateforme “emploi accompagné” du département ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="agreement_signed_ea",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec une Entreprise adaptée ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="agreement_signed_ft",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec les acteurs du réseau pour l’emploi (France Travail, Cap Emploi et Mission locale) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_ca_mad",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                verbose_name="quel était le montant annuel de votre chiffre d'affaires (Compte 706) issu exclusivement des contrats de mise à disposition de travailleurs et travailleuses handicapés (MAD) auprès d'utilisateurs tiers (entreprises, collectivités, associations) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_commercial_deficit",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_commercial_excedent",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_diversity",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                verbose_name="quel a été le montant des investissements pour diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en n-1 ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_social_deficit",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_social_excedent",
            field=models.CharField(
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
        migrations.AlterField(
            model_name="esatanswer",
            name="comments",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="nous arrivons à la fin du questionnaire. Ce champ libre vous permet d'apporter toute précision complémentaire ou de clarifier certaines informations si nécessaire. Merci de faire référence aux questions en utilisant leur identifiant (exemple : Rubrique “Aide à la mobilité”, Question c), la donnée n'est pas disponible car nous n'avons pas l'information pour 2 des 5 travailleurs concernés.)",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="documents_falclist",
            field=django.contrib.postgres.fields.ArrayField(
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
                size=None,
                verbose_name="au 31 décembre n-1, les principaux documents destinés aux travailleurs et travailleuses étaient-ils accessibles en FALC ou en communication alternative augmentée ? (contrat d'accompagnement par le travail, livret d'accueil, règlement de fonctionnement, etc.)",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="esat_name",
            field=models.CharField(blank=True, null=True, verbose_name="quel est le nom de l’ESAT ?"),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="formation_subject",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="quels ont été les sujets des formations dispensées, en interne, par l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="managing_organization_name",
            field=models.CharField(blank=True, null=True, verbose_name="quel est l’organisme gestionnaire ?"),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="mean_pct_esat_rem",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En % du SMIC",
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="au 31 décembre n-1, quel était le % moyen de rémunération directe du travailleur pris en charge par l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="mix_qvt_in_place",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="en n-1, une instance mixte (salarié(e)s/travailleurs et travailleuses) sur la qualité de vie au travail (QVT), l'hygiène et la sécurité et l'évaluation des risques professionnels est-elle en place ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_conv_exit_agreement",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="combien de conventions d'appui sont en vigueur au 31 décembre n-1 dans l'ESAT avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d'un travailleur en milieu ordinaire ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_delegate_hours",
            field=models.BooleanField(blank=True, null=True, verbose_name="si oui, précisez le nombre d'heures"),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_employee_worked",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="En nombre de personnes",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre n-1, combien de salariés ou d'agents publics (ESAT publics) étaient employés dans l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_insertion_dispo",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="On parle ici de professionnels formés et exclusifs sur la mission d'inclusion. Répondre ici en ETP",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre n-1, combien de postes de conseillers en parcours d'insertion ou assimilé étaient mis à disposition ou mutualisés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_insertion_staff",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="On parle ici de professionnels formés et exclusifs sur la mission d'inclusion. Répondre ici en ETP",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre n-1, combien de conseillers en parcours d'insertion ou assimilé étaient dans vos effectifs ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_acc",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="en n-1, combien de travailleurs et travailleuses avez-vous accompagnés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_cpf_unused",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active parmi tous les travailleurs accompagnés en n-1",
                null=True,
                verbose_name="au 31 décembre n-1, et depuis leur admission dans l'ESAT, combien de travailleurs et travailleuses ont utilisé leur CPF ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_esrp",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont suivi une formation en établissement et service de réadaptation professionnelle (ESRP/ESPO/UEROS) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_ft_job_seekers",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (effectif physique) en file active parmi ceux ayant acté dans leur projet leur volonté d'aller vers le milieu ordinaire de travail",
                null=True,
                verbose_name="combien de travailleurs et travailleuses se sont inscrits comme demandeurs d'emploi à France Travail ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_half_time",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="en n-1, combien de travailleurs et travailleuses étaient à temps partiel ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_asso",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé non lucratif (associations) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_ea",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi en entreprise adaptée ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_private",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé lucratif ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_public",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active parmi ceux partis au cours de l’année n-1",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire public ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mad_indiv",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition individuelle ou collective chez employeur public ou privé ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mispe_mdph",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de personnes (effectif physique) accueillies en n-1",
                null=True,
                verbose_name="combien de personnes ont été accompagnées par l'ESAT dans le cadre d'une mise en situation professionnelle (MISPE) prescrite par une MDPH ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mispe_rpe",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de personnes (effectif physique) accueillies en n-1",
                null=True,
                verbose_name="combien de personnes ont été accompagnées par l'ESAT dans le cadre d'une mise en situation professionnelle (MISPE) prescrite par le réseau pour l'emploi (RPE) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_new",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) parmi ceux admis en n-1",
                null=True,
                verbose_name="combien de travailleurs et travailleuses de l'ESAT ont été admis pour la première fois en milieu protégé de travail ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_only_inside",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="nombre de travailleurs et travailleuses étant resté travailler dans les murs sans contact avec le public ou le milieu ordinaire de travail ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_previous_mot",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) parmi ceux admis en n-1",
                null=True,
                verbose_name="combien de travailleurs ont occupé un emploi en milieu ordinaire (y compris entreprise adaptée) antérieurement à leur admission dans l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_service",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont réalisé une prestation de service auprès d'une entreprise, d'une collectivité publique ou de tout autre organisme ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_transport",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="b. Combien de travailleurs et travailleuses ont bénéficié d'un transport financé ou organisé par l'ESAT ? (transport en commun et/ou navette et/ou taxi)",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="pct_opco",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En %",
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="quel a été le taux de votre contribution à l'OPCO Santé ou à l'ANFH ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="pmsmp_refused",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="avez-vous eu des refus de PMSMP par les organismes du réseau pour l'emploi (France Travail, Cap Emploi, Mission Locale) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="prescription_delegate",
            field=models.BooleanField(
                blank=True, null=True, verbose_name="êtes-vous délégataire de prescription de PMSMP ?"
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="profit_sharing_bonus",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En euros. Possibilité de mettre 0.",
                null=True,
                verbose_name="en n-1, quel était le montant moyen de la prime d'intéressement (au sens de l'article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="retirement_preparation_actions",
            field=django.contrib.postgres.fields.ArrayField(
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
                        ("WORKING_HOURS_REDUCTION_AND_ORGANISATION", "Aménagement / réduction du temps de travail"),
                        ("PSYCHOLOGICAL_AND_SOCIAL_ASSISTANCE", "Actions de transition psychologique et sociale"),
                        ("OTHER", "Autres"),
                    ]
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="quelles ont été les actions conduites par l'ESAT pour préparer les travailleurs et travailleuses au départ à la retraite ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="retirement_preparation_nb_workers",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié d'actions de préparation à la retraite ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="worker_delegate",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="en n-1, y-a-t-il dans l'ESAT un.e délégué.e des travailleurs élu.e ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="worker_delegate_hours_credit",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="en n-1, est-ce que le délégué a bénéficié d'un crédit d'heures chaque mois pour remplir sa mission ?",
            ),
        ),
    ]
