from django.contrib import admin
from .models import UserBid

# Register your models here.
class UserBidAdmin(admin.ModelAdmin):
    # list_display = ['owner','created']
    fields = ['owner', 'bid']
    list_display = ('get_owner', 'get_bid')

    def get_owner(self, obj):
        return obj.owner.name
    def get_bid(self, obj):
        return obj.bid.title
#     # def get_bid(self, obj):
    #     return "\n".join([p.title for p in obj.bid.all()])
# admin.site.register(UserBid)
admin.site.register(UserBid, UserBidAdmin)