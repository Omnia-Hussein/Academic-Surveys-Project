from django.conf.urls import url
from django.urls import reverse_lazy
from .views import AcademicYearCreate

app_name = 'academic'
urlpatterns = [
    # url(r'^$', ProfessorList.as_view(), name="list"),
    # url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', AcademicYearCreate.as_view(success_url=reverse_lazy('professor:list')), name="create"),
    # url(r'^(?P<slug>\d+)/update$', ProfessorUpdate.as_view(), name="update"),
]
