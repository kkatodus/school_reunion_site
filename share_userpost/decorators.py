from django.shortcuts import redirect

def login_required(view_function):
    def wrapper(_,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts/login")
        else:
            return view_function(_,request,*args,**kwargs)
    return wrapper
 