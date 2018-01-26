from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Admin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=Admin)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()
