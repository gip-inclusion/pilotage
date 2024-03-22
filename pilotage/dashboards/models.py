from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    title = models.fields.CharField("Titre", max_length=100)

    def __str__(self):
        return f"{self.title}"


class Dashboard(models.Model):
    class Meta:
        verbose_name = "Tableau de bord"
        verbose_name_plural = "Tableaux de bord"

    title = models.fields.CharField("Titre", max_length=150)
    baseline = models.fields.CharField(max_length=250)
    slug = models.fields.SlugField()
    description = models.fields.TextField(null=True, blank=True)
    metabase_db_id = models.fields.IntegerField("Metabase ID")
    tally_popup_id = models.fields.CharField(
        "Tally Popup ID", null=True, blank=True, max_length=10
    )
    tally_embed_id = models.fields.CharField(
        "Tally Embed ID", null=True, blank=True, max_length=10
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="Categorie",
    )
    active = models.fields.BooleanField("Actif", default=True)
    new = models.fields.BooleanField("Nouveau", default=False)

    def __str__(self):
        return f"{self.title}"
