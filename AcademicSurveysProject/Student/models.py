from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    id_number = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='ID number',
    )
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    mobile_number = models.CharField(
        max_length=15,
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
        return self.name
