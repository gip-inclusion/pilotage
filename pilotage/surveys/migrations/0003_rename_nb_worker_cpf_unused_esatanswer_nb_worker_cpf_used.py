from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0002_increase_budget_fields_max_value"),
    ]

    operations = [
        migrations.RenameField(
            model_name="esatanswer",
            old_name="nb_worker_cpf_unused",
            new_name="nb_worker_cpf_used",
        ),
    ]
