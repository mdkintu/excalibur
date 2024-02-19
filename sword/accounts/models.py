from django.db import models
from django.contrib.auth.models import Group, Permission

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

