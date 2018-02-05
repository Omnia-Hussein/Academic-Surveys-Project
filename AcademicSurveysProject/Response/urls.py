from django.conf.urls import url

from .views import ResponseAnswerCreate, ResponseList, ResponseRead, ResponseAnswerUpdate

app_name = 'response'
urlpatterns = [
    url(r'^$', ResponseList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)$', ResponseRead.as_view(), name="read"),
    url(r'^(?P<id>\d+)/create$', ResponseAnswerCreate.as_view(), name="create"),
    url(r'^(?P<slug>\d+)/update$', ResponseAnswerUpdate.as_view(), name="update"),
]
