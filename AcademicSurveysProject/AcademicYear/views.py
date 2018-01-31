from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .models import AcademicYear


class AcademicYearCreate(CreateView):
    model = AcademicYear
    fields = ('year',)
    template_name = 'AcademicYear/academic_year_form.html'


class AcademicYearUpdate(UpdateView):
    model = AcademicYear
    fields = ('year',)
    template_name = 'AcademicYear/academic_year_form.html'


class AcademicYearOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'AcademicYear/academic_year_option.html')


class AcademicYearRead(DetailView):
    model = AcademicYear
    template_name = 'AcademicYear/academic_year_read.html'


class AcademicYearList(ListView):
    model = AcademicYear
    template_name = 'AcademicYear/academic_year_list.html'
