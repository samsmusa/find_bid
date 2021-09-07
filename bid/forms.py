from django.forms import ModelForm
from .models import UserBid
from django import forms

class PlaceBid(ModelForm):
    class Meta:
        model = UserBid
        fields = []