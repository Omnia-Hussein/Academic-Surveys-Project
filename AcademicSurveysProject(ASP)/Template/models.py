from django.db import models


class Template(models.Model):
    name = models.CharField(
        max_length=400,
    )
    description = models.TextField(
        max_length=4000,
    )

    def __str__(self):
        return self.name
