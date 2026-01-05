# ruff: noqa: E501
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("surveys", "0010_rename_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esatanswer",
            name="annual_ca",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                verbose_name="quel était votre chiffre d'affaire annuel commercial tout confondu (productions propres, prestations de service, mises à disposition de travailleurs et travailleuses auprès d’utilisateurs) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_diversity",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                verbose_name="quel a été le montant des investissements permettant de diversifier les activités proposées aux travailleurs et travailleuses, réalisés par l'ESAT en n-1 ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="budget_social",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SURPLUS", "excédentaire"),
                    ("BALANCE", "à l'équilibre"),
                    ("DEFICIT", "déficitaire"),
                    ("DO_NOT_KNOW", "Je ne sais pas"),
                ],
                help_text="Budget de fonctionnement dit aussi budget social",
                null=True,
                verbose_name="sur le résultat de clôture de votre Budget de Fonctionnement (Section d'Exploitation du Budget Social), étiez-vous :",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="gift_voucher_annual_budget",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel est le budget annuel de l'ESAT pour les chèques cadeaux ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="holiday_voucher_annual_budget",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En euros",
                null=True,
                verbose_name="quel est le budget annuel de l'ESAT pour les chèques vacances ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="mean_seniority",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="En nombre d'années",
                max_digits=3,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre n-1, quelle était l’ancienneté moyenne des travailleurs et travailleuses accompagnés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="mean_worker_age",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="En nombre d'années",
                max_digits=3,
                null=True,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(80)],
                verbose_name="au 31 décembre n-1, quel était l’âge moyen des travailleurs et travailleuses accompagnés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_delegate_hours",
            field=models.BooleanField(
                blank=True,
                help_text="Nombre d'heures par mois",
                null=True,
                verbose_name="si oui, précisez le nombre d'heures",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_employee_worked",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="En équivalent temps plein (ETP), salariés ou agents publics encore en poste au 31/12/n-1 et ceux partis dans l'année",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="combien de salarié(e)s ou d’agents publics (ESAT publics) ont travaillé dans l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_esat_agreement",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre d'ESAT",
                null=True,
                verbose_name="avec combien d'ESAT avez-vous conventionné pour garantir l’exercice du droit au retour ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_insertion_dispo",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont mis à disposition ou mutualisés ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_insertion_staff",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="On parle ici de professionnels formés et exclusifs sur la mission d’inclusion. Répondre ici en ETP",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="au 31 décembre, combien de postes de conseillers en parcours d'insertion ou chargé(e)s d'inclusion professionnelle sont dans vos effectifs ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_support_hours",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                help_text="Nombre d'heures en moyenne par travailleur sur année n-1",
                max_digits=4,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="quel était le nombre d’heures de soutien liées à l’activité professionnelle, dont en moyenne chaque travailleur a bénéficié (rémunérées et comprises dans le temps de travail) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_acc",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="combien de travailleurs et travailleuses avez-vous accompagné ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_cpf_unused",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs en file active",
                null=True,
                verbose_name="au 31 décembre n-1, et depuis leur admission dans l'ESAT, combien de travailleurs et travailleuses ont utilisé leur CPF ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_cumul_esat_ea",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT et un emploi à temps partiel en Entreprise Adaptée ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_cumul_esat_mot",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont cumulé un temps partiel dans l'ESAT avec un emploi à temps partiel en milieu ordinaire classique, privé ou public ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_formation_opco",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs en file active",
                null=True,
                verbose_name="en n-1, combien de travailleurs et travailleuses de l'ESAT ont suivi une formation prise en charge par l'OPCO Santé ou par l’ANFH ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_ft_job_seekers",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs parmi ceux ayant acté dans leur projet leur volonté d'aller vers le MOT",
                null=True,
                verbose_name="combien de travailleurs et travailleuses se sont inscrits comme demandeurs d’emploi à France Travail ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_half_time",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) en file active",
                null=True,
                verbose_name="parmi eux, combien de travailleurs et travailleuses étaient à temps partiel ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs partis au cours de l'année n-1",
                null=True,
                verbose_name="en n-1, combien de travailleurs et travailleuses ont quitté l'ESAT ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_asso",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Y compris intérim",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé non lucratif (associations) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_ea",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Y compris intérim",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi en entreprise adaptée ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_private",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Y compris intérim",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire privé lucratif ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_left_public",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Y compris intérim",
                null=True,
                verbose_name="combien ont quitté l'ESAT pour un emploi dans le milieu ordinaire public ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mispe_mdph",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de personnes (effectif physique) accueillies en n-1",
                null=True,
                verbose_name="combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par une MDPH ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_mispe_rpe",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de personnes (effectif physique) accueillies en n-1",
                null=True,
                verbose_name="combien de personnes ont été accueillies par l'ESAT dans le cadre d’une mise en situation professionnelle (MISPE) prescrite par le réseau pour l'emploi (RPE) ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_new",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) parmi les travailleurs admis en n-1",
                null=True,
                verbose_name="quel était le nombre de travailleurs et travailleuses dans l'ESAT admis pour la première fois en milieu protégé ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_other_esat_with_agreement",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs",
                null=True,
                verbose_name="parmi eux, combien ont réintégré un ESAT avec lequel vous aviez conclu une convention de retour ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_previous_mot",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) parmi les travailleurs admis en n-1",
                null=True,
                verbose_name="quel était le nombre de travailleurs et travailleuses dans l'ESAT ayant occupé antérieurement à leur admission un emploi en milieu ordinaire y compris adapté ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_temporary",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="En nombre de travailleurs (effectif physique) parmi les travailleurs admis en n-1",
                null=True,
                verbose_name="combien de travailleurs et travailleuses ont été admis temporairement dans l'ESAT pour remplacer des travailleurs absents pour maladie, pour suivre une action formation ou pour occuper un emploi à temps partiel ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="nb_worker_willing_mot",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Nombre de travailleurs",
                null=True,
                verbose_name="combien de travailleurs de l'ESAT ont exprimé dans leur projet personnalisé leur volonté d’aller travailler en milieu ordinaire ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="pct_opco",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="en %",
                null=True,
                validators=[django.core.validators.MaxValueValidator(100)],
                verbose_name="quel a été le taux de votre contribution à l’OPCO Santé ou à l’ANFH ?",
            ),
        ),
        migrations.AlterField(
            model_name="esatanswer",
            name="profit_sharing_bonus",
            field=models.PositiveSmallIntegerField(
                blank=True,
                null=True,
                verbose_name="en n-1, quel était le montant moyen de la prime d’intéressement (au sens de l’article R 243-6 du CASF) versée aux travailleurs et travailleuses?",
            ),
        ),
    ]
