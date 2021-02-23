from django.shortcuts import redirect, render

def login_required(view_function):
    def wrapper(_,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts/login")
        else:
            return view_function(_,request,*args,**kwargs)
    return wrapper


def open_to_user_groups(user_groups,redirect_html):
    def decorator(view_function):
        def wrapper(_,request,*args,**kwargs):
            group = None
            if request.user.groups.filter(name__in=user_groups).exists() or request.user.is_admin:
                return view_function(_,request,*args,**kwargs)
            return render(request,redirect_html)
        return wrapper
    return decorator

 