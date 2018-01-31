from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Course


class CourseCreate(CreateView):
    model = Course
    fields = ('name', 'code', 'academic_year', 'department', 'is_active',)
    template_name = 'Course/course_form.html'


class CourseUpdate(UpdateView):
    model = Course
    fields = ('name', 'code', 'academic_year', 'department', 'is_active',)
    template_name = 'Course/course_update.html'


class CourseOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Course/course_option.html')


class CourseRead(DetailView):
    model = Course
    template_name = 'Course/course_read.html'


class CourseList(ListView):
    model = Course
    template_name = 'Course/course_list.html'
