from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

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
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # Add other fields as needed
