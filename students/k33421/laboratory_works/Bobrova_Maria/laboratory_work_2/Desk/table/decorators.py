from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import redirect


def student_required():
    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            if requset.user.is_student:
                return view_func(requset, *args, **kwargs)
            else:
                return HttpResponse('You are not student')
        return wrapper_func

    return decorator


def additional_info_check():
    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            if requset.user.with_additional_info:
                return view_func(requset, *args, **kwargs)
            else:
                return redirect("add_info")

        return wrapper_func

    return decorator


def teacher_required():
    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            if requset.user.is_teacher:
                return view_func(requset, *args, **kwargs)
            else:
                return HttpResponse('You are not teacher')
        return wrapper_func

    return decorator


def allowed_users(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            group = None
            if requset.users.exists():
                group = requset.users.groups.all()[0].name

            if group in allowed_roles:
                return view_func(requset, *args, **kwargs)
            else:
                return HttpResponse('You are not student')

        return wrapper_func

    return decorator