from django.conf.urls import url
from django.urls import reverse_lazy

from .views import TemplateQuestionCreate, TemplateList, TemplateQuestionUpdate, TemplateRead, TemplateOption, \
    TemplateSurvey

app_name = 'template'
urlpatterns = [
    url(r'^$', TemplateOption.as_view(), name="option"),
    url(r'^(?P<pk>\d+)$', TemplateRead.as_view(), name="read"),
    url(r'^list$', TemplateList.as_view(), name='list'),
    url(r'^create$', TemplateQuestionCreate.as_view(success_url=reverse_lazy('template:list')), name="create"),
    url(r'^(?P<pk>\d+)/update$', TemplateQuestionUpdate.as_view(success_url=reverse_lazy('template:list')),
        name="update"),
    url(r'^(?P<pk>\d+)/survey', TemplateSurvey.as_view(), name="survey"),
]
