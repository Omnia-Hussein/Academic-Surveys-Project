from django.views.generic import CreateView

from .models import Department


class DepartmentCreate(CreateView):
    model = Department
    fields = ('name',)
    template_name = 'Department/department_form.html'
