from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
import uuid

class CustomUser(models.Model):
    # ... your custom fields 
    groups = models.ManyToManyField(
        Group,
        blank=True, 
        related_name="custom_users"  # Change here
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="custom_users"  # Change here
    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30, blank=True)
    username=models.CharField(max_length=254, unique=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True)  # Already included in the default User model
    github = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    

    def __str__(self):
        return f"{self.user}"
    
class Message(models.Model):
    sender=models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    receiver=models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)
    subject=models.CharField(max_length=200, null=True, blank=True)
    body=models.TextField()
    is_read=models.BooleanField(default=False, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering=['is_read','-created']