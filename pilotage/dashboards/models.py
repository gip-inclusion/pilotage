from django.db import models

class Dashboard(models.Model):
    title = models.fields.CharField(max_length=100)
