# ruff: noqa: E501

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0008_survey_opening_period"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="esatanswer",
            name="annual_health_complementary_budget",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="health_complementary",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="pct_employee_activity_bonus",
        ),
        migrations.RemoveField(
            model_name="esatanswer",
            name="pct_health_complementary_esat",
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="insertion_staff_funding",
            field=models.CharField(
                blank=True,
                choices=[
                    ("BPAS", "Par votre budget de fonctionnement (BPAS)"),
                    ("BAPC", "Par votre budget annexe de production et de commercialisation (BAPC)"),
                ],
                null=True,
                verbose_name="comment sont-ils financés ?",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="nb_conv_exit_agreement_new",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="combien de conventions d'appui ont été signées dans l'année n-1 avec un employeur privé ou public pour accompagner la sortie et le parcours professionnel d'un travailleur en milieu ordinaire ?",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="nb_employee_reverse_duoday",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="en n-1, combien de professionnels du milieu ordinaire ont participé à des Duoday inversés ?",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="nb_worker_left_other_reason",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="combien ont quitté l'ESAT pour d'autres raisons ?"
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="nb_worker_only_inside",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="nombre de travailleurs et travailleuses étant resté travailler dans les murs sans contact avec le public ou le MOT",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="nb_worker_other_esat_with_agreement",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="parmi eux, combien ont réintégré un ESAT avec lequel vous aviez conclu une convention de retour ?",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="skills_validation_type",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="quels ont été les types de dispositifs dont ont bénéficié les travailleurs et travailleuses de l'ESAT pour reconnaitre et développer leurs compétences ?",
            ),
        ),
        migrations.AddField(
            model_name="esatanswer",
            name="software_name",
            field=models.TextField(blank=True, null=True, verbose_name="logiciel utilisé"),
        ),
    ]
