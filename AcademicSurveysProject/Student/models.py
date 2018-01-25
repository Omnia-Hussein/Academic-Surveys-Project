from django.db import models
from Home.models import User


class Student(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    secondary_email = models.EmailField(
        max_length=100,
    )
    FRESH = 'fr'
    OTHER = 'ot'
    TYPE_CHOICES = (
        (FRESH, 'Fresh'),
        (OTHER, 'Other'),
    )
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=FRESH,
    )

    @property
    def __str__(self):
        return self.user.username
