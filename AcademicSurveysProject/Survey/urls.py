from django.conf.urls import url
from django.urls import reverse_lazy
from .views import SurveyQuestionCreate, SurveyList, SurveyQuestionUpdate

app_name = 'survey'
urlpatterns = [
    url(r'^$', SurveyList.as_view(), name="list"),
    # url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', SurveyQuestionCreate.as_view(success_url=reverse_lazy('survey:list')), name="create"),
    url(r'^(?P<pk>\d+)/update$', SurveyQuestionUpdate.as_view(success_url=reverse_lazy('survey:list')), name="update"),
]
