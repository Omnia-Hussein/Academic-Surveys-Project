from .models import Department
from django.views.generic import CreateView


class DepartmentCreate(CreateView):
    model = Department
    fields = ('name',)
    template_name = 'Department/department_form.html'
