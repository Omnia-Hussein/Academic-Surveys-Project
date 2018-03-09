from django.conf.urls import url
from django.urls import reverse_lazy

from .views import CourseCreate, CourseOption, CourseList, CourseRead, CourseUpdate

app_name = 'course'
urlpatterns = [
    url(r'^$', CourseOption.as_view(), name="option"),
    url(r'^list$', CourseList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)$', CourseRead.as_view(), name="read"),
    url(r'^create$', CourseCreate.as_view(success_url=reverse_lazy('course:list')), name="create"),
    url(r'^(?P<pk>\d+)/update$', CourseUpdate.as_view(success_url=reverse_lazy('course:list')), name="update"),
]
