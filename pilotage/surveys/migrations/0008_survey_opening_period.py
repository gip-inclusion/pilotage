import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0007_remove_answer_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="opening_period",
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(
                default=(None, None), verbose_name="période d'ouverture"
            ),
            preserve_default=False,
        ),
    ]
