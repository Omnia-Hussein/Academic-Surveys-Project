from django.conf.urls import url

from .views import HomeOption

app_name = 'home'
urlpatterns = [
    url(r'^$', HomeOption.as_view(), name="option"),
]
