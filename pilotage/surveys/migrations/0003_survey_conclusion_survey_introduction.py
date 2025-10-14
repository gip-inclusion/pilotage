from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0002_add_esat_survey_and_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="conclusion",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="survey",
            name="introduction",
            field=models.TextField(blank=True, null=True),
        ),
    ]
