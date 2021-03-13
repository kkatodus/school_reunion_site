from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse
from user.models import *
import json
from django.core import serializers
from django.forms.models import model_to_dict
import requests



def index(request):
    room_list = Room.objects.order_by('-created_at')[:]
    template = loader.get_template('chat/index.html')
    context = {
        'room_list': room_list,
    }
    return HttpResponse(template.render(context, request))

def chat(request, room_name):
    messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
    message_for_list = Message.objects.filter(room__name=room_name).distinct('user')
    room = Room.objects.filter(name=room_name)[0]
    person = str(request.user)
    template = loader.get_template('chat/chat_room.html')
    context = {
        'messages': messages,
        'room': room,
        'person':person,
        'messages_for_list':message_for_list
    }
    return HttpResponse(template.render(context, request))

def room(request):
    name = request.POST.get("room_name")
    room = Room.objects.create(name=name)
    return HttpResponseRedirect(reverse('chat:chat_room', args=[name]))
