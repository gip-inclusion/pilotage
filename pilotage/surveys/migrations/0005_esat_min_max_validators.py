# ruff: noqa: E501
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0004_esat_do_not_know_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="mean_employee_age",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=3,
                null=True,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)],
                verbose_name="au 31 décembre n-1, quel était l’âge moyen des travailleurs et travailleuses accompagnés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="mean_pct_esat_rem",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="au 31 décembre n-1, quel était le montant moyen de la part rémunération garantie du travailleur prise en charge financièrement par l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="mean_seniority",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="L'ancienneté moyenne doit être exprimée en mois",
                max_digits=3,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre n-1, quelle était l’ancienneté moyenne des travailleurs et travailleuses accompagnés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_employee_worked",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Combien de salarié(e)s ou d’agents publics (ESAT publics) ont été employés dans l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_places_allowed",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre n-1, quel était l'agrément fixé par l'ARS pour l'ESAT en nombre de places autorisées ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="pct_ca_public",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="indiquez le pourcentage de votre chiffre d'affaires réalisé avec des clients du secteur public",
            ),
        ),
    ]
