from django.contrib import admin
from .models import Profile, Bids

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','created']
admin.site.register(Profile, ProfileAdmin)

class BidsAdmin(admin.ModelAdmin):
    list_display = ['title', 'state','published', 'end']
admin.site.register(Bids, BidsAdmin)