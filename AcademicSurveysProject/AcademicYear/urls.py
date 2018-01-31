from django.conf.urls import url
from django.urls import reverse_lazy

from .views import AcademicYearCreate, AcademicYearList, AcademicYearOption, AcademicYearRead, AcademicYearUpdate

app_name = 'academic_year'
urlpatterns = [
    url(r'^$', AcademicYearOption.as_view(), name="option"),
    url(r'^list$', AcademicYearList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)$', AcademicYearRead.as_view(), name="read"),
    url(r'^create$', AcademicYearCreate.as_view(success_url=reverse_lazy('academic_year:list')), name="create"),
    url(r'^(?P<pk>\d+)/update$', AcademicYearUpdate.as_view(success_url=reverse_lazy('academic_year:list')),
        name="update"),
]
