from django.core.exceptions import PermissionDenied


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
