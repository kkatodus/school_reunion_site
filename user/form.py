from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser
from allauth.account.adapter import DefaultAccountAdapter

class CustomUserSignupForm(SignupForm):
    date_moved_to_germany = forms.DateField(required=False)
    years_in_germany = forms.IntegerField(required=False)

    class Meta:
        model = CustomUser

    def signup(self,request,user):
        user.date_moved_to_germany = self.cleaned_data["date_moved_to_germany"]
        user.years_in_germany = self.cleaned_data["years_in_germany"]
        user.save()
        return user
    