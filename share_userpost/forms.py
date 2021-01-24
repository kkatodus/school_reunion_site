from .models import UserPost
from django import forms

class UserPostCreationForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ("text","image")