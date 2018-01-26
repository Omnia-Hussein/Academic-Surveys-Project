from django.db import models


class AcademicYear(models.Model):
    PREPARATORY = 'pr'
    FIRST = 'fi'
    SECOND = 'se'
    THIRD = 'th'
    FORTH = 'fo'
    YEAR_CHOICES = (
        (PREPARATORY, 'Preparatory'),
        (FIRST, 'First'),
        (SECOND, 'Second'),
        (THIRD, 'Third'),
        (FORTH, 'Forth'),
    )
    year = models.CharField(
        max_length=2,
        choices=YEAR_CHOICES,
        default=PREPARATORY,
        unique=True,
    )

    @property
    def __str__(self):
        return AcademicYear.YEAR_CHOICES[self.year]
