# ruff: noqa: E501
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0004_more_help_texts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_delegate_hours",
            field=models.BooleanField(
                blank=True,
                help_text="Nombre d'heures par mois. Désolés, nous avons inversé les champs. Répondez à cette question dans le champ d'après (d)",
                null=True,
                verbose_name="si oui, précisez le nombre d'heures",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="worker_delegate_hours_credit",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Désolés, nous avons inversé les champs. Répondez cette question dans le champ d'avant (c)",
                null=True,
                verbose_name="en n-1, est-ce que le délégué a bénéficié d'un crédit d'heures chaque mois pour remplir sa mission ?",
            ),
        ),
    ]
