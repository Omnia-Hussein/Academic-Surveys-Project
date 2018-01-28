from django.conf.urls import url
from django.urls import reverse
from .views import CourseCreate

app_name = 'course'
urlpatterns = [
    # url(r'^$', ProfessorList.as_view(), name="list"),
    # url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', CourseCreate.as_view(success_url='professor:list'), name="create"),
    # url(r'^(?P<slug>\d+)/update$', ProfessorUpdate.as_view(), name="update"),
]
