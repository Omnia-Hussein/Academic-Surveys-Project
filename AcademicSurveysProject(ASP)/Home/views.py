from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.views import View

from Response.models import Response
from Survey.models import Survey


class HomeOption(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            if request.user.is_admin:
                return self.home_admin(request, *args, **kwargs)
            elif request.user.is_professor:
                return self.home_professor(request, *args, **kwargs)
            return self.home_student(request, *args, **kwargs)
        return self.home_unauthenticated(request, *args, **kwargs)

    @staticmethod
    def home_admin(request, *args, **kwargs):
        return render(request, 'Home/home_admin.html')

    @staticmethod
    def home_student(request, *args, **kwargs):
        surveys = Survey.objects.filter(course__students__user_id=request.user.id).all()
        surveys_completed = []
        surveys_uncompleted = []
        responses = []
        for survey in surveys:
            response = Response.objects.filter(student_id=request.user.id, survey_id=survey.id).first()
            if response:
                responses += [response]
                surveys_completed += [survey]
            else:
                surveys_uncompleted += [survey]
        context = {'surveys_completed': surveys_completed,
                   'surveys_uncompleted': surveys_uncompleted,
                   'responses': responses}
        return render(request, 'Home/home_student.html', context)

    @staticmethod
    def home_professor(request, *args, **kwargs):
        surveys = Survey.objects.filter(professor_id=request.user.id).all()
        surveys_active = []
        surveys_inactive = []
        for survey in surveys:
            if survey.is_active:
                surveys_active += [survey]
            else:
                surveys_inactive += [survey]
        context = {'surveys_active': surveys_active,
                   'surveys_inactive': surveys_inactive}
        return render(request, 'Home/home_professor.html', context)

    @staticmethod
    def home_unauthenticated(request, *args, **kwargs):
        return render(request, 'Home/home_unauthenticated.html')


def bad_request(request):
    response = render(request, 'Home/400.html')
    response.status_code = 400
    return response


def permission_denied(request):
    response = render(request, 'Home/403.html')
    response.status_code = 403
    return response


def page_not_found(request):
    response = render(request, 'Home/404.html')
    response.status_code = 404
    return response


def server_error(request):
    response = render(request, 'Home/500.html')
    response.status_code = 500
    return response


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Home/change_password.html', {
        'form': form
    })
