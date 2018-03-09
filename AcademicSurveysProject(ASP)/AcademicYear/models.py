from django.db import models

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


class AcademicYear(models.Model):
    year = models.CharField(
        max_length=2,
        choices=YEAR_CHOICES,
        default=PREPARATORY,
        unique=True,
    )

    def __str__(self):
        return dict(YEAR_CHOICES).get(self.year)
