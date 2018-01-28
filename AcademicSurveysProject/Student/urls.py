from django.conf.urls import url
from .views import StudentList, StudentRead, StudentCreate, StudentUpdate

app_name = 'student'
urlpatterns = [
    url(r'^$', StudentList.as_view(), name="list"),
    url(r'^(?P<slug>\d+)$', StudentRead.as_view(), name="read"),
    url(r'^create$', StudentCreate.as_view(success_url='student:list'), name="create"),
    url(r'^(?P<slug>\d+)/update$', StudentUpdate.as_view(), name="update"),
]
