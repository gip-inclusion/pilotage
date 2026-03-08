from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0014_add_step_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="title",
            field=models.CharField(blank=True, null=True, verbose_name="titre"),
        ),
    ]
