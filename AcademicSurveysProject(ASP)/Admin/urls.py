from django.conf.urls import url
from django.urls import reverse_lazy

from .views import AdminList, AdminRead, AdminCreate, AdminUpdate, AdminOption

app_name = 'administrator'
urlpatterns = [
    url(r'^$', AdminOption.as_view(), name="option"),
    url(r'^list$', AdminList.as_view(), name="list"),
    url(r'^(?P<slug>\d+)$', AdminRead.as_view(), name="read"),
    url(r'^create$', AdminCreate.as_view(success_url=reverse_lazy('administrator:list')), name="create"),
    url(r'^(?P<slug>\d+)/update$', AdminUpdate.as_view(success_url=reverse_lazy('administrator:list')), name="update"),
]
