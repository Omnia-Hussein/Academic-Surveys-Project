from django.db import models

from AcademicYear.models import AcademicYear
from Department.models import Department


class Course(models.Model):
    name = models.CharField(
        max_length=200,
    )
    code = models.CharField(
        max_length=200,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name
