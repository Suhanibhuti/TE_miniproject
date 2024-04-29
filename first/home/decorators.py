from django.shortcuts import redirect
# from .models import CustomUser
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def _wrapped_func(request,*args, **kwargs ):
        if request.user.is_authenticated:
            return redirect('homes')
        else:
            return view_func(request,*args, **kwargs)
    return _wrapped_func

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            # print("working:",allowed_roles)
            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:                
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def student_only(view_func):
    def wrapper_func(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name 
        if group == "mentor":
            return redirect('loginpageM')
        if group == "student":
            return view_func(request,*args, **kwargs)
        
    return wrapper_func 

# def student_required(view_func):
#     def _wrapped_view(request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.role == CustomUser.STUDENT:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('loginpage')
#     return _wrapped_view

# def mentor_required(view_func):
#     def _wrapped_view(request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.role == CustomUser.MENTOR:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('loginpageM')
#     return _wrapped_view