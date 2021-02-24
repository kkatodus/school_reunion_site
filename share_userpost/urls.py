from django.urls import path
from . import views
from user.views import UserDetailView,UserProfileEditView

app_name = "share_userpost"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("event",views.EventView.as_view(),name="event"),
    path("all_posts",views.AllPostsView.as_view(),name="all_posts"),
    path("self_posts",views.SelfPostsView.as_view(),name="self_posts"),
    path("userpost-detail/<int:post_id>",views.PostDetailView.as_view(),name="detail"),
    path("userpost-detail/delete-post/<int:post_id>",views.DeletePostView.as_view(),name="delete"),
    path("userpost-detail/user/detail/<int:user_id>",UserDetailView.as_view(),name="user_detail"),
    path("userpost-detail/user/detail/edit/<int:user_id>",UserProfileEditView.as_view(),name="user_profile_edit")
]