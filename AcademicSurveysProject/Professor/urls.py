from django.conf.urls import url
from .views import ProfessorList, ProfessorRead, ProfessorCreate, ProfessorUpdate

app_name = 'professor'
urlpatterns = [
    url(r'^$', ProfessorList.as_view(), name="list"),
    url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', ProfessorCreate.as_view(success_url='professor:list'), name="create"),
    url(r'^(?P<slug>\d+)/update$', ProfessorUpdate.as_view(), name="update"),
]
