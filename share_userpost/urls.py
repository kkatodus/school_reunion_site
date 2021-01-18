from django.urls import path
from . import views

app_name = "share_userpost"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("event",views.EventView.as_view(),name="event"),
    path("photos",views.PhotosView.as_view(),name="photos")
]