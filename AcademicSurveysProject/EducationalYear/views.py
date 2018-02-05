from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from AcademicSurveysProject.decorators import admin_required
from .models import EducationalYear


@method_decorator([login_required, admin_required], name='dispatch')
class EducationalYearCreate(CreateView):
    model = EducationalYear
    fields = ('start_year', 'end_year',)
    template_name = 'EducationalYear/educational_year_form.html'


@method_decorator([login_required, admin_required], name='dispatch')
class EducationalYearUpdate(UpdateView):
    model = EducationalYear
    fields = ('start_year', 'end_year',)
    template_name = 'EducationalYear/educational_year_form.html'


@method_decorator([login_required, admin_required], name='dispatch')
class EducationalYearOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'EducationalYear/educational_year_option.html')


@method_decorator([login_required, admin_required], name='dispatch')
class EducationalYearRead(DetailView):
    model = EducationalYear
    template_name = 'EducationalYear/educational_year_read.html'


@method_decorator([login_required, admin_required], name='dispatch')
class EducationalYearList(ListView):
    model = EducationalYear
    template_name = 'EducationalYear/educational_year_list.html'
