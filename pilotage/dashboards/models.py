from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"

    title = models.fields.CharField(verbose_name="titre", max_length=100)

    def __str__(self):
        return f"{self.title}"


class Dashboard(models.Model):
    class Meta:
        verbose_name = "tableau de bord"
        verbose_name_plural = "tableaux de bord"

    title = models.fields.CharField(verbose_name="titre", max_length=150)
    baseline = models.fields.CharField(max_length=250)
    slug = models.fields.SlugField()
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="catégorie",
    )
    metabase_db_id = models.fields.IntegerField(verbose_name="metabase ID")
    description = models.fields.TextField(null=True, blank=True)
    tally_popup_id = models.fields.CharField(verbose_name="tally popup ID", null=True, blank=True, max_length=10)
    tally_embed_id = models.fields.CharField(verbose_name="tally embed ID", null=True, blank=True, max_length=10)
    active = models.fields.BooleanField(verbose_name="actif", default=True)
    new = models.fields.BooleanField(verbose_name="nouveau", default=False)

    def __str__(self):
        return f"{self.title}"
