from django.shortcuts import render, redirect

from share_userpost.decorators import login_required
from django.views import View
from .models import CustomUser
from .form import UserProfileCreationForm
# Create your views here.

class UserDetailView(View):
    profile_detail_template = "profile/user_profile_detail.html"
    profile_creation_template = "profile/user_profile_creation.html"

    @login_required
    def get(self,request,user_id=None, *args, **kwargs):
        user = CustomUser.objects.get(id=user_id)
        if user.profile:
            print("user has profile")
            return render(request,self.profile_detail_template)
        else:
            print("user does not have profile")
            form = UserProfileCreationForm()
            context = {"form":form}
            return render(request,self.profile_creation_template, context)

    def post(self,request,user_id=None, *args, **kwargs):
        user = CustomUser.objects.get(id=user_id)
        user_profile_form = UserProfileCreationForm(request.POST,request.FILES)
        profile = user.profile
        print(user_profile_form)
        if user_profile_form.is_valid():
            user_profile_instance = user_profile_form.save(commit=True)
            if user.profile:           
                user.profile = None
                profile.delete()     
            user.profile = user_profile_instance
            user.save()
        else:
            print("Form is not valid mate")
        return redirect("share_userpost:home")

class UserProfileEditView(UserDetailView):
    profile_edit_template = "profile/user_profile_edit.html"
    
    @login_required
    def get(self, request, user_id=None,*args, **kwargs):
        user = CustomUser.objects.get(id=user_id)
        data = [(user.profile.date_moved_to_germany,"date_moved_to_germany","text"),
                (user.profile.years_in_germany,"years_in_germany","number")]
        context = {"data":data}
        return render(request, self.profile_edit_template)