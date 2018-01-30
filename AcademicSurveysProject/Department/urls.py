from django.conf.urls import url

from .views import DepartmentCreate

app_name = 'department'
urlpatterns = [
    # url(r'^$', ProfessorList.as_view(), name="list"),
    # url(r'^(?P<slug>\d+)$', ProfessorRead.as_view(), name="read"),
    url(r'^create$', DepartmentCreate.as_view(success_url='professor:list'), name="create"),
    # url(r'^(?P<slug>\d+)/update$', ProfessorUpdate.as_view(), name="update"),
]
