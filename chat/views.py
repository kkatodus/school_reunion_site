from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse
from user.models import *
import json
from django.core import serializers
from django.forms.models import model_to_dict
import sys
from django.views import generic,View
from django.views.decorators.csrf import ensure_csrf_cookie




def index(request):
    room_list = Room.objects.order_by('-created_at')[:5]
    template = loader.get_template('chat/index.html')
    context = {
        'room_list': room_list,
    }
    return HttpResponse(template.render(context, request))

def chat(request, room_name):
    messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
    room = Room.objects.filter(name=room_name)[0]
    image = CustomUser.objects.get(username=request.user).profile.profile_picture.url
    template = loader.get_template('chat/chat_room.html')
    context = {
        'messages': messages,
        'room': room,
    }
    return HttpResponse(template.render(context, request))

def room(request):
    name = request.POST.get("room_name")
    room = Room.objects.create(name=name)
    return HttpResponseRedirect(reverse('chat:chat_room', args=[name]))
