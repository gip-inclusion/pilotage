import django.db.models.deletion
from django.db import migrations, models

import pilotage.surveys.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("kind", models.CharField(choices=[], verbose_name="type")),
                ("vintage", models.CharField(verbose_name="millésime")),
                ("name", models.SlugField(editable=False, unique=True, verbose_name="nom")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="créé le")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="mis à jour le")),
            ],
            options={
                "verbose_name": "enquête",
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=pilotage.surveys.models._uuid7, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "en cours"), ("done", "terminé")],
                        default="pending",
                        verbose_name="statut",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="créé le")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="mis à jour le")),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="surveys.survey",
                        verbose_name="enquête",
                    ),
                ),
            ],
            options={
                "verbose_name": "réponse",
            },
        ),
    ]
