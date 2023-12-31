from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatRoom(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message_content = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',) # this will retrieve messages from db based on date order.