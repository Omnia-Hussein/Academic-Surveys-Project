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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from AcademicSurveysProject.decorators import public_required
from Home.views import change_password

handler400 = 'Home.views.bad_request'
handler403 = 'Home.views.permission_denied'
handler404 = 'Home.views.page_not_found'
handler500 = 'Home.views.server_error'

urlpatterns = [
    url(r'^password_reset/$', public_required(auth_views.password_reset), name='password_reset'),
    url(r'^password_reset/done/$', public_required(auth_views.password_reset_done), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^login/$', public_required(auth_views.login), {'template_name': 'Home/user_login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^change_password/$', login_required(change_password), name='change_password'),
    url(r'^administrator/', admin.site.urls),
    url(r'^', include('Home.urls')),
    url(r'^student/', include('Student.urls')),
    url(r'^professor/', include('Professor.urls')),
    url(r'^admin/', include('Admin.urls')),
    url(r'^survey/', include('Survey.urls')),
    url(r'^academic_year/', include('AcademicYear.urls')),
    url(r'^educational_year/', include('EducationalYear.urls')),
    url(r'^department/', include('Department.urls')),
    url(r'^course/', include('Course.urls')),
    url(r'^response/', include('Response.urls')),
    url(r'^template/', include('Template.urls')),
]
