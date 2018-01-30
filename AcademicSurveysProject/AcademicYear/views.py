from django.views.generic import CreateView

from .models import AcademicYear


class AcademicYearCreate(CreateView):
    model = AcademicYear
    fields = ('year',)
    template_name = 'AcademicYear/academic_year_form.html'
