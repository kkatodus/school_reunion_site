from django.urls import path
from . import views

app_name = "share_userpost"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("event",views.EventView.as_view(),name="event"),
    path("all_posts",views.AllPostsView.as_view(),name="all_posts"),
    path("self_posts",views.SelfPostsView.as_view(),name="self_posts"),
]