from .models import EducationalYear
from django.views.generic import CreateView


class EducationalYearCreate(CreateView):
    model = EducationalYear
    fields = ('start_year', 'end_year',)
    template_name = 'EducationalYear/educational_year_form.html'
