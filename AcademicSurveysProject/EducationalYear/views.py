from django.views.generic import CreateView

from .models import EducationalYear


class EducationalYearCreate(CreateView):
    model = EducationalYear
    fields = ('start_year', 'end_year',)
    template_name = 'EducationalYear/educational_year_form.html'
