from django.views.generic import CreateView

from .models import Course


class CourseCreate(CreateView):
    model = Course
    fields = ('name', 'code', 'academic_year', 'department',)
    template_name = 'Course/course_form.html'
