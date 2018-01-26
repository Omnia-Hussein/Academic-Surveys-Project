from django.db import models


class EducationalYear(models.Model):
    start_year = models.IntegerField(
        max_length=4,
    )
    end_year = models.IntegerField(
        max_length=4,
    )

    class Meta:
        unique_together = (
            'start_year',
            'end_year',
        )

    @property
    def __str__(self):
        return '%s/%s' % (self.start_year, self.end_year)
