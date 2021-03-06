import uuid
from django.db import models
from django.utils import timezone
from user.models import CustomUser

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey(
        Room,
        blank=True,
        null=True,
        related_name='room_messages',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(CustomUser,blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
