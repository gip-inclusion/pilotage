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
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="Categorie",
    )
    metabase_db_id = models.fields.IntegerField("Metabase ID")
    description = models.fields.TextField(null=True, blank=True)
    tally_popup_id = models.fields.CharField(
        "Tally Popup ID", null=True, blank=True, max_length=10
    )
    tally_embed_id = models.fields.CharField(
        "Tally Embed ID", null=True, blank=True, max_length=10
    )
    active = models.fields.BooleanField("Actif", default=True)
    com_alert = models.fields.BooleanField("Encart actif", default=False)
    com_alert_description = models.fields.CharField(
        max_length=250,
        default="Enquête utilisateur : votre avis est précieux pour nous aider à améliorer nos tableaux de bord !",
    )
    com_alert_text = models.fields.CharField(
        max_length=500,
        default="Jusqu’au 20 octobre, prenez part à notre enquête sur l'usage des tableaux de bord dans vos missions et partagez vos suggestions d'amélioration.",
    )
    com_alert_link = models.fields.CharField(
        max_length=150, default="https://tally.so/r/nPYGJd"
    )
    new = models.fields.BooleanField("Nouveau", default=False)

    def __str__(self):
        return f"{self.title}"
