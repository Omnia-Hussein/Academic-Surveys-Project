from django.conf.urls import url
from django.urls import reverse_lazy

from .views import ProfessorList, ProfessorRead, ProfessorCreate, ProfessorUpdate, ProfessorOption

app_name = 'professor'
urlpatterns = [
    url(r'^$', ProfessorOption.as_view(), name="option"),
    url(r'^list$', ProfessorList.as_view(), name="list"),
    url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', ProfessorCreate.as_view(success_url=reverse_lazy('professor:list')), name="create"),
    url(r'^(?P<slug>\d+)/update$', ProfessorUpdate.as_view(success_url=reverse_lazy('professor:list')), name="update"),
]
