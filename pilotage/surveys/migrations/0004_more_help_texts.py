# ruff: noqa: E501
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0003_rename_nb_worker_cpf_unused_esatanswer_nb_worker_cpf_used"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="after_skills_validation",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) partis au cours de l’année n-1",
                null=True,
                verbose_name="parmi les travailleurs sortis dans l’année, combien avaient obtenu une validation ou une reconnaissance de leurs compétences en amont ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_ca",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel était votre chiffre d'affaire annuel commercial tout confondu (productions propres, prestations de service, mises à disposition de travailleurs et travailleuses auprès d'utilisateurs) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_ca_mad",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel était le montant annuel de votre chiffre d'affaires (Compte 706) issu exclusivement des contrats de mise à disposition de travailleurs et travailleuses handicapés (MAD) auprès d'utilisateurs tiers (entreprises, collectivités, associations) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_ca_production",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel était votre chiffre d'affaire annuel commercial en productions propres ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_ca_service",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel était votre chiffre d'affaire annuel commercial en prestation de service ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_accessibility",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel a été le montant des investissements de mise aux normes de sécurité et d'accessibilité des installations réalisés par l'ESAT en n-1 ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_diversity",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel a été le montant des investissements pour diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en n-1 ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_delegate_hours",
            field=models.BooleanField(
                blank=True,
                help_text="Nombre d'heures par mois",
                null=True,
                verbose_name="si oui, précisez le nombre d'heures",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_autodetermination",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié dans l'année d'une formation à l'autodétermination ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_esrp",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont suivi une formation en établissement et service de réadaptation professionnelle (ESRP/ESPO/UEROS) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_rae_rsfp",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié d'une RAE ou d'une RSFP ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_reinteg",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="nombre de travailleurs et travailleuses ayant réintégré l'ESAT",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_reinteg_other",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="nombre de travailleurs et travailleuses ayant intégré un autre ESAT",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_vae",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié d'une VAE ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_worked_sunday",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses de l'ESAT ont travaillé au moins un dimanche ou un jour férié en n-1 ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="pct_ca_public",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En %",
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="indiquez le pourcentage de votre chiffre d'affaires réalisé avec des clients du secteur public",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="pct_more_than50",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="combien de travailleurs ou travailleuses de plus de 50 ans ont travaillé dans l'ESAT en n-1 ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="retirement_preparation_nb_workers",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs (personnes physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont bénéficié d'actions de préparation à la retraite ?",
            ),
        ),
    ]
