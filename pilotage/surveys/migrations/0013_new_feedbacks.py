# ruff: noqa: E501

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0012_new_partnership_agreement_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="esatanswer",
            name="software_name",
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="after_skills_validation",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
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
                    ]
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="a l’issue de cette reconnaissance ou validation, quelle a été la suite du parcours des travailleurs et travailleuses concerné(e)s ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_transport_budget",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel budget annuel avez-vous alloué au transport des travailleurs et travailleuses de leur domicile à l’ESAT (transport en commun et/ou navette et/ou taxi) ?",
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
                help_text="Le facile à lire et à comprendre (FALC) est une méthode qui a pour but de traduire un langage classique en un langage simplifié.",
                null=True,
                size=None,
                verbose_name="au 31 décembre n-1, les principaux documents destinés aux travailleurs et travailleuses étaient-ils accessibles en FALC ou en communication alternative augmentée ? (contrat d’accompagnement par le travail, livret d’accueil, règlement de fonctionnement, etc.)",
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
            name="mean_pct_esat_rem",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En % du SMIC",
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="au 31 décembre n-1, quel était le montant moyen de la part rémunération garantie du travailleur prise en charge financièrement par l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_code",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont le code ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_cumul_esat_ea",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT et un emploi à temps partiel en Entreprise Adaptée ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_cumul_esat_mot",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT avec un emploi à temps partiel en milieu ordinaire classique, privé ou public ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_driving_licence",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont leur permis de conduire ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mad_collec",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition collective d'un employeur public ou privé ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mad_indiv",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont réalisé une mise à disposition individuelle d'un employeur public ou privé ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mobility_inclusion_card",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié de la carte mobilité inclusion ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_only_inside",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="nombre de travailleurs et travailleuses étant resté travailler dans les murs sans contact avec le public ou le MOT",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_pmsmp",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont effectué une PMSMP ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_service",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont réalisé une prestation de service auprès d'une entreprise, d'une collectivité publique ou de tout autre organisme, assurée avec ou un plusieurs salarié(e)s de l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_transport",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié d'un transport proposé par l'ESAT? (transport en commun et/ou navette et/ou taxi)",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_with_public",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="nombre de travailleurs et travailleuses ayant réalisé une activité dans un lieu au contact de la clientèle ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="profit_sharing_bonus",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="en euros. Possibilité de mettre 0",
                null=True,
                verbose_name="en n-1, quel était le montant moyen de la prime d’intéressement (au sens de l’article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
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
                        ("UAAT", "Inscription dans la démarche Un Avenir Après le Travail"),
                        (
                            "MEETING_SCHEDULED",
                            "Organisation d’un RDV avec un professionnel compétent sur le sujet (Assistante sociale, RH, Directeur/-trice, etc.)",
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
            name="skills_validation_type",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("RAE", "Reconnaissance des acquis de l'expérience (RAE)"),
                        ("RSFP", "Reconnaissance des savoir-faire professinnels (RSFP)"),
                        ("VAE", "Validation des acquis de l'expérience (VAE)"),
                        ("AFEST", "Action de formation en situation de travail (AFEST)"),
                        ("OTHER", "Autres actions"),
                        ("NONE", "Aucune"),
                    ]
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="quels ont été les types de dispositifs dont ont bénéficié les travailleurs et travailleuses de l'ESAT pour reconnaitre et développer leurs compétences ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="support_themes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("WORKSHOP_JOB_SEARCH", "Atelier d'accompagnement à la recherche d'emplois"),
                        ("WORKSHOP_WELLBEING", "Ateliers de prévention santé / bien-être au travail"),
                        ("PROFESSIONAL_SUPPORT", "Soutien professionnel"),
                        ("CPF_OPENED", "Ouverture du Compte Professionnel de Formation"),
                        ("COMPANY_TOUR", "Visites dans les entreprises"),
                        ("COMPANY_PREMISES_MORNING_TOUR", "Matinées entreprises dans les locaux"),
                    ]
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="sur quelles thématiques principales ?",
            ),
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="worker_delegate",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="worker_delegate",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="en n-1, y-a-t-il dans l'ESAT un délégué/une déléguée des travailleurs élu(e) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="worker_delegate_formation",
            field=models.CharField(
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
        migrations.RemoveField(
            model_name="esatanswer",
            name="worker_delegate_hours_credit",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="worker_delegate_hours_credit",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="est-ce que le délégué ou la déléguée bénéficie d'un crédit d'heures chaque mois pour remplir sa mission ?",
            ),
        ),
    ]
