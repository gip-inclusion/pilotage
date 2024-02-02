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

    title = models.fields.CharField("Titre", max_length=100)
    baseline = models.fields.CharField(max_length=100)
    slug = models.fields.SlugField()
    description = models.fields.TextField(null=True, blank=True)
    metabase_db_id = models.fields.IntegerField("Metabase ID")
    tally_id = models.fields.CharField(
        "Tally Popup ID", null=True, blank=True, max_length=10
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Categorie",
    )
    active = models.fields.BooleanField("Actif", default=True)

    def __str__(self):
        return f"{self.title}"
