from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import EducationalYear


class EducationalYearCreate(CreateView):
    model = EducationalYear
    fields = ('start_year', 'end_year',)
    template_name = 'EducationalYear/educational_year_form.html'


class EducationalYearUpdate(UpdateView):
    model = EducationalYear
    fields = ('start_year', 'end_year',)
    template_name = 'EducationalYear/educational_year_form.html'


class EducationalYearOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'EducationalYear/educational_year_option.html')


class EducationalYearRead(DetailView):
    model = EducationalYear
    template_name = 'EducationalYear/educational_year_read.html'


class EducationalYearList(ListView):
    model = EducationalYear
    template_name = 'EducationalYear/educational_year_list.html'
