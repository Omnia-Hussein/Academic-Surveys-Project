from django.conf.urls import url
from django.urls import reverse_lazy

from .views import ResponseAnswerCreate, ResponseList

app_name = 'response'
urlpatterns = [
    url(r'^$', ResponseList.as_view(), name="list"),
    # url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^(?P<id>\d+)/create$', ResponseAnswerCreate.as_view(success_url=reverse_lazy('response:list')), name="create"),
    # url(r'^(?P<slug>\d+)/update$', ResponseAnswerUpdate.as_view(), name="update"),
]
