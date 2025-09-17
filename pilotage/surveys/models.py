import uuid_utils
from django.db import models
from django.utils.text import slugify


def _uuid7():
    # TODO: Replace by the stdlib function when moving to Python 3.14.
    return str(uuid_utils.uuid7())


class SurveyKind(models.TextChoices):
    pass


class Survey(models.Model):
    kind = models.CharField(verbose_name="type", choices=SurveyKind.choices)
    vintage = models.CharField(verbose_name="millésime")
    name = models.SlugField(verbose_name="nom", unique=True, editable=False)

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "enquête"

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.name = self.name or slugify(f"{self.kind} {self.vintage}")
        super().save(**kwargs)


class AnswerStatus(models.TextChoices):
    PENDING = "pending", "en cours"
    DONE = "done", "terminé"


class Answer(models.Model):
    uid = models.UUIDField(primary_key=True, default=_uuid7, editable=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="answers", verbose_name="enquête")
    status = models.CharField(verbose_name="statut", default=AnswerStatus.PENDING, choices=AnswerStatus.choices)

    created_at = models.DateTimeField(verbose_name="créé le", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="mis à jour le", auto_now=True)

    class Meta:
        verbose_name = "réponse"

    def __str__(self):
        return str(self.uid)
