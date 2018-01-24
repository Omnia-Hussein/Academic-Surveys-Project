from django.conf.urls import url
from Professor import views
urlpatterns = [
    # /student/
    url(r'^$', views.index, name="student_index"),

    # # /student/15
    # url(r'^(?P<student_id>[0-9]+)$', views.read, name="read"),

    # /student/create
    url(r'^create$', views.create, name="create"),

    # # /student/15/edit
    # url(r'^(?P<st_id>[0-9]+)/edit$', views.update, name="update"),
    #
    # # /student/15/delete
    # url(r'^(?P<st_id>[0-9]+)/delete$', views.delete, name="delete"),
]
