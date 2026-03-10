from django.db import migrations, models

import pilotage.itoutils.validators


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0018_update_support_themes_choices"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="esatanswer",
            name="managing_organization_name",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="managing_organization_finess",
            field=models.CharField(
                blank=True,
                max_length=9,
                null=True,
                validators=[pilotage.itoutils.validators.validate_finess],
                verbose_name="quel est le numéro FINESS de l’entité juridique de rattachement ?",
            ),
        ),
    ]
