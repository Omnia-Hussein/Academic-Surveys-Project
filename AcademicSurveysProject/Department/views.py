from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from AcademicSurveysProject.decorators import admin_required
from .models import Department


@method_decorator([login_required, admin_required], name='dispatch')
class DepartmentCreate(CreateView):
    model = Department
    fields = ('name',)
    template_name = 'Department/department_form.html'


@method_decorator([login_required, admin_required], name='dispatch')
class DepartmentUpdate(UpdateView):
    model = Department
    fields = ('name',)
    template_name = 'Department/department_update.html'


@method_decorator([login_required, admin_required], name='dispatch')
class DepartmentOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Department/department_option.html')


@method_decorator([login_required, admin_required], name='dispatch')
class DepartmentRead(DetailView):
    model = Department
    template_name = 'Department/department_read.html'


@method_decorator([login_required, admin_required], name='dispatch')
class DepartmentList(ListView):
    model = Department
    template_name = 'Department/department_list.html'
