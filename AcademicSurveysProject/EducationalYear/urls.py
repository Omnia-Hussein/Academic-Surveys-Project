from django.conf.urls import url

from .views import EducationalYearCreate, EducationalYearList, EducationalYearOption, EducationalYearRead, \
    EducationalYearUpdate

app_name = 'educational_year'
urlpatterns = [
    url(r'^$', EducationalYearOption.as_view(), name="option"),
    url(r'^list$', EducationalYearList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)$', EducationalYearRead.as_view(), name="read"),
    url(r'^create$', EducationalYearCreate.as_view(success_url='educational_year:list'), name="create"),
    url(r'^(?P<pk>\d+)/update$', EducationalYearUpdate.as_view(success_url='educational_year:list'), name="update"),
]
