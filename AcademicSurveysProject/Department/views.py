from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Department


class DepartmentCreate(CreateView):
    model = Department
    fields = ('name',)
    template_name = 'Department/department_form.html'


class DepartmentUpdate(UpdateView):
    model = Department
    fields = ('name',)
    template_name = 'Department/department_update.html'


class DepartmentOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Department/department_option.html')


class DepartmentRead(DetailView):
    model = Department
    template_name = 'Department/department_read.html'


class DepartmentList(ListView):
    model = Department
    template_name = 'Department/department_list.html'
