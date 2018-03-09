from django.db import models


class EducationalYear(models.Model):
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (
            'start_year',
            'end_year',
        )

    def __str__(self):
        # return "{}/{}".format(self.start_year, self.end_year,)
        return '%d/%d' % (self.start_year, self.end_year)
