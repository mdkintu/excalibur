# accounts/signals.py
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            email=instance.email,
            username=instance.username,
            name=instance.first_name + ' ' + instance.last_name
        )

        subject='Welcome to Nsangi Guest Wing'
        message='We are glad to see to you'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, 
            [instance.email],
            fail_silently=False,
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        profile = Profile.objects.get(user=instance)
        profile.delete()
    except Profile.DoesNotExist:
        pass

def updateUser(sender, instance, **kwargs):
    profile=instanceuser=profile.user

    if created ==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()