from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.urls import reverse

from Course.models import Course


class Professor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    secondary_email = models.EmailField(
        max_length=100,
    )
    courses = models.ManyToManyField(
        Course,
        related_name='professors',
        blank=True,
    )

    @property
    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=Professor)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()
