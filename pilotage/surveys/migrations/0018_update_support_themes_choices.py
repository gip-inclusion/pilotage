import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0017_update_fields_wordings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="support_themes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("WORKSHOP_JOB_SEARCH", "Atelier d'accompagnement à la recherche d'emploi"),
                        ("WORKSHOP_WELLBEING", "Atelier de prévention santé / bien-être au travail"),
                        ("PROFESSIONAL_SUPPORT", "Activité de soutien au parcours professionnel"),
                        ("CPF_OPENED", "Ouverture du Compte Professionnel de Formation"),
                        ("COMPANY_TOUR", "Visites dans les entreprises"),
                        ("PREMISES_TOUR", "Visites des locaux de l’ESAT par les entreprises"),
                        ("OTHER", "Autres"),
                    ]
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="sur quelles thématiques principales ?",
            ),
        ),
    ]
