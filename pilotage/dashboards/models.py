"""
Champs a créer
- title
- baseline
- slug (html encode)
- description (long text)
- metabase_db_id
- categorie (dans une autre base ou un array)
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

class Dashboard(models.Model):
    class Category(models.TextChoices):
        VUE_ENSEMBLE = 'VUE_ENSEMBLE', _('Vue d’ensemble')
        RECRUTEMENT = 'RECRUTEMENT', _('Recrutement')
        PRESCRIPTEURS = 'PRESCRIPTEURS', _('Prescripteurs')
        EMPLOYEURS_INCLUSIFS = 'EMPLOYEURS_INCLUSIFS', _('Employeurs inclusifs')
        PUBLICS = 'PUBLICS', _('Publics')
        STATISTIQUES_DES_SERVICES = 'STATISTIQUES_DES_SERVICES', _('Statistiques des services de la Plateforme de l’inclusion')

    title = models.fields.CharField(max_length=100)
    baseline = models.fields.CharField(max_length=100)
    slug = models.fields.SlugField()
    description = models.fields.TextField(null=True, blank=True)
    metabase_db_id = models.fields.IntegerField()
    category = models.fields.CharField(choices=Category.choices, max_length=50, default=Category.VUE_ENSEMBLE)
