from .models import UserPost
from django import forms

class UserPostCreationForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    class Meta:
        model = UserPost
        fields = ("text","image")