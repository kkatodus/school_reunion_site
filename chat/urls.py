'''

from django.urls import path, include

from .views import *

app_name = 'chat'
urlpatterns = [
    path('', index, name='index' ),
    path('<str:room_name>/', chat, name= 'chat_room'),
    path('room/', room, name = 'room')
]
'''
from user.views import UserDetailView, UserProfileEditView
from django.urls import include, path
from .views import *


app_name = 'chat'
urlpatterns = [
    path('', index, name='index'),
    path('chat/<str:room_name>/', chat, name='chat_room'),
    path('room/', room, name='room'),
    path("user/detail/<int:user_id>",UserDetailView.as_view(),name="user_detail"),
    path("user/detail/edit/<int:user_id>",UserProfileEditView.as_view(),name="user_profile_edit"),
    path("chat/<str:room_name>/user/detail/<int:user_id>",UserDetailView.as_view(),name="user_detail"),
    path("chat/<str:room_name>/user/detail/edit/<int:user_id>",UserProfileEditView.as_view(),name="user_profile_edit"),
]