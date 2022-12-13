from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_user(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args,**kwargs):
            group=None
            if request.user.groups.exists():
               group= request.user.groups[0]
               if group in allowed_roles:
                return view_func(request,*args,**kwargs)
               else:
                    return HttpResponse('Unauthorised user')
        return wrapper_func