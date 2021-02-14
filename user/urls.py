from django.urls import path,include
from . import views

app_name = "user"

urlpatterns = [
    path("detail",views.UserDetailView.as_view(),name="detail"),
]