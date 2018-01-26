from django.db import models


class Department(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )

    @property
    def __str__(self):
        return self.name
