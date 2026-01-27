# ruff: noqa: E501

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0005_esat_min_max_validators"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_insertion_dispo",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="On parle ici de professionnels formés et exclusifs sur la mission d'inclusion. Répondre ici en ETP.",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont mis à disposition ou mutualisés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_insertion_staff",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="On parle ici de professionnels formés et exclusifs sur la mission d'inclusion. Répondre ici en ETP.",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont dans vos effectifs ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_support_hours",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="quel était le nombre d'heures de soutien liées à l'activité professionnelle, dont en moyenne chaque travailleur a bénéficié (rémunérées et comprises dans le temps de travail) ?",
            ),
        ),
    ]
