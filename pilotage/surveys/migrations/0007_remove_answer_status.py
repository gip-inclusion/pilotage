from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0006_alter_esatanswer_nb_insertion_dispo_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="status",
        ),
    ]
