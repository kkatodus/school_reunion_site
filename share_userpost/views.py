from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserPost

# Create your views here.


class HomeView(generic.TemplateView,LoginRequiredMixin):
    template_name = "home.html"

class EventView(generic.TemplateView,LoginRequiredMixin):
    template_name = "event.html"

class PhotosView(generic.ListView, LoginRequiredMixin):
    template_name = "photos.html"
    model = UserPost    