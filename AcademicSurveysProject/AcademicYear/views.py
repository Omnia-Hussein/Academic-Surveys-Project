from .models import AcademicYear
from django.views.generic import CreateView


class AcademicYearCreate(CreateView):
    model = AcademicYear
    fields = ('year',)
    template_name = 'AcademicYear/academic_year_form.html'
