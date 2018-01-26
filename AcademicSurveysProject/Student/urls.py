"""AcademicSurveysProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Student import views

urlpatterns = [
    # /student/
    url(r'^$', views.index, name="student_list"),

    # /student/15
    url(r'^(?P<student_id_number>[0-9]+)$', views.read, name="read"),

    # /student/create
    url(r'^create$', views.create, name="create"),

    # # /student/15/edit
    # url(r'^(?P<st_id>[0-9]+)/edit$', views.update, name="update"),
    #
    # # /student/15/delete
    # url(r'^(?P<st_id>[0-9]+)/delete$', views.delete, name="delete"),
]
