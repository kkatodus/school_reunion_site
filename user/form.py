from allauth.account.forms import SignupForm
from django.forms import ModelForm
from .models import CustomUser, UserProfile
from allauth.account.adapter import DefaultAccountAdapter

class CustomUserSignupForm(SignupForm):
    class Meta:
        model = CustomUser

    def signup(self,request,user):
        user.save()
        return user

class UserProfileCreationForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_picture","date_moved_to_germany","years_in_germany"]