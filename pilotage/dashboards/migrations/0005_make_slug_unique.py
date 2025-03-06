from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboards", "0004_remove_charfield_max_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dashboard",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
