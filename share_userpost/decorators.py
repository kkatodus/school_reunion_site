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
            print(f"Allowed User Groups:{user_groups}")
            group = None
            if not request.user.groups.filter(name__in=user_groups).exists():
                print(f"Requesting user group:{request.user.groups}")
                return render(request,redirect_html)
            return view_function(_,request,*args,**kwargs)
        return wrapper
    return decorator

 