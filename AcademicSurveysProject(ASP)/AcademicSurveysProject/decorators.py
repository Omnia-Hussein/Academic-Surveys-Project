from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from Response.models import Response
from Survey.models import Survey


def public_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            raise PermissionDenied
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def professor_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_professor:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def student_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_student:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_or_professor_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin or request.user.is_professor:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_or_profile_professor_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin or (request.user.is_professor and request.user.id_number == int(kwargs['slug'])):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_or_profile_student_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin or (request.user.is_student and request.user.id_number == int(kwargs['slug'])):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_or_response_student_owner_required(function):
    def wrap(request, *args, **kwargs):
        response = get_object_or_404(Response, pk=kwargs['pk'])
        if request.user.is_admin or (request.user.is_student and response.student_id is request.user.id):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_or_survey_professor_owner_required(function):
    def wrap(request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['pk'])
        if request.user.is_admin or (request.user.is_professor and survey.professor_id is request.user.id):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def response_student_course_required(function):
    def wrap(request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['id'])
        if request.user.is_student and survey.course.students.filter(user_id=request.user.id).first() is not None:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def response_student_owner_required(function):
    def wrap(request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['slug'])
        response = get_object_or_404(Response, survey_id=survey.id)
        if request.user.is_student and response.student_id is request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def survey_professor_owner_required(function):
    def wrap(request, *args, **kwargs):
        survey = get_object_or_404(Survey, pk=kwargs['pk'])
        if request.user.is_professor and survey.professor_id is request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

# if scorm.objects.filter(Header__id=qp.id).exists():
