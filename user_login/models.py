from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext as _


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    short_intro = models.TextField(max_length=200, null=True, blank=True)
    bio = models.TextField()
    profiel_image = models.ImageField(null=True, blank=True, upload_to='images/', default="images/banner.png")
    social_facebook = models.URLField(null=True, blank=True)
    social_twitter = models.URLField(null=True, blank=True)
    social_github = models.URLField(null=True, blank=True)
    social_website = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
        primary_key=True, editable=False,
        )

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-created']


class Bids(models.Model):
    # id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("title"), max_length=500)
    state = models.CharField(_("state"), max_length=255, null=True, blank=True)
    published = models.CharField(_("published"), max_length=255, null=True, blank=True)
    end = models.CharField(_("closed"), max_length=255,null=True, blank=True)

    def __str__(self) -> str:
            return self.title

    class Meta:
        ordering = ['-published']