from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from AcademicSurveysProject.decorators import admin_required
from .models import AcademicYear


@method_decorator([login_required, admin_required], name='dispatch')
class AcademicYearCreate(CreateView):
    model = AcademicYear
    fields = ('year',)
    template_name = 'AcademicYear/academic_year_form.html'


@method_decorator([login_required, admin_required], name='dispatch')
class AcademicYearUpdate(UpdateView):
    model = AcademicYear
    fields = ('year',)
    template_name = 'AcademicYear/academic_year_form.html'


@method_decorator([login_required, admin_required], name='dispatch')
class AcademicYearOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'AcademicYear/academic_year_option.html')


@method_decorator([login_required, admin_required], name='dispatch')
class AcademicYearRead(DetailView):
    model = AcademicYear
    template_name = 'AcademicYear/academic_year_read.html'


@method_decorator([login_required, admin_required], name='dispatch')
class AcademicYearList(ListView):
    model = AcademicYear
    template_name = 'AcademicYear/academic_year_list.html'
