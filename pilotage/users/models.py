from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class UserGroup(AbstractUser):
    EDITOR = "EDITOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (EDITOR, "Éditeur"),
        (SUBSCRIBER, "Abonné"),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="rôle")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.EDITOR:
            group = Group.objects.get(name="editors")
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name="subscribers")
            group.user_set.add(self)
