from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from AcademicSurveysProject.decorators import admin_required
from .models import Course


@method_decorator([login_required, admin_required], name='dispatch')
class CourseCreate(CreateView):
    model = Course
    fields = ('name', 'code', 'academic_year', 'department', 'is_active',)
    template_name = 'Course/course_form.html'


@method_decorator([login_required, admin_required], name='dispatch')
class CourseUpdate(UpdateView):
    model = Course
    fields = ('name', 'code', 'academic_year', 'department', 'is_active',)
    template_name = 'Course/course_update.html'


@method_decorator([login_required, admin_required], name='dispatch')
class CourseOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Course/course_option.html')


@method_decorator([login_required, admin_required], name='dispatch')
class CourseRead(DetailView):
    model = Course
    template_name = 'Course/course_read.html'


@method_decorator([login_required, admin_required], name='dispatch')
class CourseList(ListView):
    model = Course
    template_name = 'Course/course_list.html'
