from django.db import models


class Category(models.Model):
    title = models.fields.CharField("Titre", max_length=100)

    def __str__(self):
        return f"{self.title}"


class Dashboard(models.Model):
    title = models.fields.CharField("Titre", max_length=100)
    baseline = models.fields.CharField(max_length=100)
    slug = models.fields.SlugField()
    description = models.fields.TextField(null=True, blank=True)
    metabase_db_id = models.fields.IntegerField("Metabase ID")
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Catégorie",
    )
    active = models.fields.BooleanField("Actif", default=True)

    def __str__(self):
        return f"{self.title}"
