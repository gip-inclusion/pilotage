from django.db import migrations, models

import pilotage.surveys.models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0019_prefill_from_finess"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="uid",
            field=models.UUIDField(
                default=pilotage.surveys.models.uuid7, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
