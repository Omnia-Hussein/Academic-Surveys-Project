from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete
from Course.models import Course
from Department.models import Department
from AcademicYear.models import AcademicYear
from EducationalYear.models import EducationalYear


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    secondary_email = models.EmailField(
        max_length=100,
    )
    FRESH = 'fr'
    GRADUATED = 'gr'
    OTHER = 'ot'
    STATUS_CHOICES = (
        (FRESH, 'Fresh'),
        (GRADUATED, 'Graduated'),
        (OTHER, 'Other'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=FRESH,
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        related_name='students',
    )
    educational_year = models.ForeignKey(
        EducationalYear,
        related_name='students',
    )
    department = models.ForeignKey(
        Department,
        related_name='students',
    )
    courses = models.ManyToManyField(
        Course,
        related_name='students',
    )

    @property
    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=Student)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()
