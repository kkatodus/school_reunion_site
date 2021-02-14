from django.shortcuts import render

from share_userpost.decorators import login_required
from django.views import View
# Create your views here.

class UserDetailView(View):
    template_name = "account/user_detail.html"
    @login_required
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)