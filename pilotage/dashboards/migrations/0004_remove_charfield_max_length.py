import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboards", "0003_alter_dashboard_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(validators=[django.core.validators.MaxLengthValidator(100)], verbose_name="titre"),
        ),
        migrations.AlterField(
            model_name="dashboard",
            name="baseline",
            field=models.CharField(validators=[django.core.validators.MaxLengthValidator(250)]),
        ),
        migrations.AlterField(
            model_name="dashboard",
            name="tally_embed_id",
            field=models.CharField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxLengthValidator(10)],
                verbose_name="tally embed ID",
            ),
        ),
        migrations.AlterField(
            model_name="dashboard",
            name="tally_popup_id",
            field=models.CharField(
                blank=True,
                null=True,
                validators=[django.core.validators.MaxLengthValidator(10)],
                verbose_name="tally popup ID",
            ),
        ),
        migrations.AlterField(
            model_name="dashboard",
            name="title",
            field=models.CharField(validators=[django.core.validators.MaxLengthValidator(150)], verbose_name="titre"),
        ),
    ]
