# ruff: noqa: E501
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0011_update_help_texts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="esatanswer",
            name="ea_convention_signed",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="esat_pea_rattached",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="nb_ea_convention_signed",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="pea_agreement_signed",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="rpe_agreement_signed",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="agreement_signed_cap_emploi",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec Cap emploi",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="agreement_signed_dept_pae",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec la plateforme accompagnée du département",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="agreement_signed_ea",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec une Entreprise adaptée",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="agreement_signed_ft",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec France Travail",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="agreement_signed_ml",
            field=models.BooleanField(
                blank=True,
                null=True,
                verbose_name="pour l'année n-1, une convention était-elle en vigueur avec Mission Locale",
            ),
        ),
    ]
