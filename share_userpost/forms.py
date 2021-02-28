from .models import UserPost, Picture
from django import forms

# class UserPostCreationForm(forms.ModelForm):
#     image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta:
#         model = UserPost
#         fields = ("text","image")


class UserPostCreationForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ("post_text",)

class PictureCreationForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ("image",)