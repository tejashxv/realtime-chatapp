from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.group_name
    
    
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_messages')
    body = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.author.username}: {self.body[:20]}..."  # Display first 20 characters of content
    
    class Meta:
        ordering = ['-created']