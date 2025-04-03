from django.core.validators import MaxLengthValidator
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"

    title = models.fields.CharField(verbose_name="titre", validators=[MaxLengthValidator(100)])
    display_order = models.fields.PositiveSmallIntegerField(verbose_name="ordre d'affichage", blank=True, default=0)

    def __str__(self):
        return f"{self.title}"


class Dashboard(models.Model):
    class Meta:
        verbose_name = "tableau de bord"
        verbose_name_plural = "tableaux de bord"

    title = models.fields.CharField(verbose_name="titre", validators=[MaxLengthValidator(150)])
    baseline = models.fields.CharField(validators=[MaxLengthValidator(250)])
    slug = models.fields.SlugField(unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="catégorie",
    )
    metabase_db_id = models.fields.IntegerField(verbose_name="metabase ID")
    embed_url = models.fields.URLField(
        verbose_name="embed URL",
        help_text="Si vous souhaitez ajouter une url d'iframe à la place d'un 'Metabase ID', "
        "vous devez de mettre 0 dans le 'Metabase ID' et ajouter une url ci-dessus",
        null=True,
        blank=True,
    )
    description = models.fields.TextField(null=True, blank=True)
    tally_popup_id = models.fields.CharField(
        verbose_name="tally popup ID", null=True, blank=True, validators=[MaxLengthValidator(10)]
    )
    tally_embed_id = models.fields.CharField(
        verbose_name="tally embed ID", null=True, blank=True, validators=[MaxLengthValidator(10)]
    )
    active = models.fields.BooleanField(verbose_name="actif", default=True)
    new = models.fields.BooleanField(verbose_name="nouveau", default=False)

    def __str__(self):
        return f"{self.title}"
