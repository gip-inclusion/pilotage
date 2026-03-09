# ruff: noqa: E501
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0015_survey_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="esatanswer",
            name="nb_worker_mad_collec",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="pct_activity_outside",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="nb_employee_shared",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="En nombre de personnes",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="parmi eux, combien étaient mutualisés sur plusieurs ESAT ?",
            ),
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="nb_worker_other_esat_with_agreement",
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_support_hours",
            field=models.CharField(
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
        migrations.RemoveField(
            model_name="esatanswer",
            name="after_skills_validation",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="after_skills_validation",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="a l'issue de cette reconnaissance ou validation, quelle a été la suite du parcours des travailleurs et travailleuses concerné(e)s ?",
            ),
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="agreement_signed_cap_emploi",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="agreement_signed_ml",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="skills_notebook_software_used",
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_commercial",
            field=models.CharField(
                blank=True,
                choices=[("SURPLUS", "excédentaire"), ("BALANCE", "à l'équilibre"), ("DEFICIT", "déficitaire")],
                null=True,
                verbose_name="sur le résultat net de la SEC, étiez-vous",
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
                verbose_name="de quel montant est-ce déficit ?",
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
                verbose_name="de quel montant est-cet excédant?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_social",
            field=models.CharField(
                blank=True,
                choices=[("SURPLUS", "excédentaire"), ("BALANCE", "à l'équilibre"), ("DEFICIT", "déficitaire")],
                help_text="Budget de fonctionnement dit aussi budget social",
                null=True,
                verbose_name="sur le résultat de clôture de votre Budget de Fonctionnement (Section d'Exploitation du Budget Social), étiez-vous :",
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
                verbose_name="de quel montant est-ce déficit ?",
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
                verbose_name="de quel montant est-cet excédant?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="insertion_staff_funding",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("BPAS", "Par votre budget de fonctionnement (BPAS)"),
                        ("BAPC", "Par votre budget annexe de production et de commercialisation (BAPC)"),
                        ("OTHER", "Autres"),
                    ]
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="comment sont-ils financés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_delegate_hours",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="est-ce que le délégué ou la déléguée bénéficie d'un crédit d'heures chaque mois pour remplir sa mission ?",
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
                verbose_name="quelles ont été les actions conduites par l'ESAT pour préparer les travailleurs et travailleuses au départ à la retraite (inscription dans la démarche Un Avenir Après le Travail, rendez-vous organisés avec la CARSAT, etc.) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="skills_notebook",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Oui"), ("NO", "Non"), ("WIP", "C'est en cours")],
                null=True,
                verbose_name="avez-vous mis en place un carnet de parcours et de compétences ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="skills_validation_type",
            field=django.contrib.postgres.fields.ArrayField(
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
                size=None,
                verbose_name="quels ont été les types de dispositifs dont ont bénéficié les travailleurs et travailleuses de l'ESAT pour reconnaitre et développer leurs compétences ?",
            ),
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="software_financial_help",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="software_financial_help",
            field=django.contrib.postgres.fields.ArrayField(
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
                size=None,
                verbose_name="l'ESAT a t-il bénéficié d'une aide financière pour mettre en place ce carnet et le cas échéant, acquérir un logiciel ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="uaat_inscription",
            field=models.CharField(
                blank=True,
                choices=[("YES", "Oui"), ("NO", "Non"), ("WIP", "C'est en cours")],
                null=True,
                verbose_name="êtes-vous inscrit dans la démarche Un Avenir Après le Travail (UAAT) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="worker_delegate_hours_credit",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre d'heures par mois",
                null=True,
                verbose_name="si oui, précisez le nombre d'heures",
            ),
        ),
    ]
