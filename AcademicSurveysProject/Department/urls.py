from django.conf.urls import url
from django.urls import reverse_lazy

from .views import DepartmentCreate, DepartmentList, DepartmentOption, DepartmentRead, DepartmentUpdate

app_name = 'department'
urlpatterns = [
    url(r'^list$', DepartmentList.as_view(), name="list"),
    url(r'^$', DepartmentOption.as_view(), name="option"),
    url(r'^(?P<pk>\d+)$', DepartmentRead.as_view(), name="read"),
    url(r'^create$', DepartmentCreate.as_view(success_url=reverse_lazy('department:list')), name="create"),
    url(r'^(?P<pk>\d+)/update$', DepartmentUpdate.as_view(success_url=reverse_lazy('department:list')), name="update"),
]
