# ruff: noqa: E501
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_transport_budget",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel budget annuel avez-vous alloué au transport des travailleurs et travailleuses de leur domicile à l'ESAT (transport en commun et/ou navette et/ou taxi) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="gift_voucher_annual_budget",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel est le budget annuel de l'ESAT pour les chèques cadeaux ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="holiday_voucher_annual_budget",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel est le budget annuel de l'ESAT pour les chèques vacances ?",
            ),
        ),
    ]
