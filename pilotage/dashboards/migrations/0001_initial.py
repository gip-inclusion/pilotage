# Generated by Django 5.0.1 on 2024-02-06 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="titre")),
            ],
            options={
                "verbose_name": "catégorie",
                "verbose_name_plural": "catégories",
            },
        ),
        migrations.CreateModel(
            name="Dashboard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="titre")),
                ("baseline", models.CharField(max_length=250)),
                ("slug", models.SlugField()),
                ("description", models.TextField(blank=True, null=True)),
                ("metabase_db_id", models.IntegerField(verbose_name="metabase ID")),
                (
                    "tally_popup_id",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="tally popup ID",
                    ),
                ),
                (
                    "tally_embed_id",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="tally embed ID",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="actif")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboards.category",
                        verbose_name="catégorie",
                    ),
                ),
            ],
            options={
                "verbose_name": "tableau de bord",
                "verbose_name_plural": "tableaux de bord",
            },
        ),
    ]
