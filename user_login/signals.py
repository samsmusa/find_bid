from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

post_save.connect(createProfile, sender=User)