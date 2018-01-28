from django.conf.urls import url
from django.urls import reverse_lazy
from .views import ResponseAnswerCreate, ResponseList

app_name = 'response'
urlpatterns = [
    url(r'^$', ResponseList.as_view(), name="list"),
    # url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', ResponseAnswerCreate.as_view(success_url=reverse_lazy('response:list')), name="create"),
    # url(r'^(?P<pk>\d+)/update$', SurveyQuestionUpdate.as_view(success_url=reverse_lazy('survey:list')), name="update"),
]
