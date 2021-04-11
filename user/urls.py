from django.urls import path,include
from . import views

app_name = "user"

urlpatterns = [
    path("detail/<int:user_id>",views.UserDetailView.as_view(),name="detail"),
    path("detail/edit/<int:user_id>",views.UserProfileEditView.as_view(),name="edit"),
    path("all_users",views.AllUsersView.as_view(), name="all_users")
]