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

from django.urls import include, path
from .views import *

app_name = 'chat'
urlpatterns = [
    path('', index, name='index'),
    path('chat/<str:room_name>/', chat, name='chat_room'),
    path('room/', room, name='room'),
]