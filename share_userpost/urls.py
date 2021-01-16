from django.urls import path
from . import views

app_name = "share_userpost"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home")
]