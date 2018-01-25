from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id_number = models.BigIntegerField(
        unique=True,
        verbose_name='ID number',
    )
    name = models.CharField(
        max_length=300,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    mobile_number = models.CharField(
        max_length=15,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_professor = models.BooleanField(
        default=False,
    )
    is_student = models.BooleanField(
        default=False,
    )
