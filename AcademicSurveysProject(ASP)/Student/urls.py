from django.conf.urls import url
from django.urls import reverse_lazy

from .views import StudentList, StudentRead, StudentCreate, StudentUpdate, StudentOption

app_name = 'student'
urlpatterns = [
    url(r'^$', StudentOption.as_view(), name="option"),
    url(r'^list$', StudentList.as_view(), name="list"),
    url(r'^(?P<slug>\d+)$', StudentRead.as_view(), name="read"),
    url(r'^create$', StudentCreate.as_view(success_url=reverse_lazy('student:list')), name="create"),
    url(r'^(?P<slug>\d+)/update$', StudentUpdate.as_view(success_url=reverse_lazy('student:list')), name="update"),
]
