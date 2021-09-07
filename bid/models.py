from django.db import models
from user_login.models import Profile, Bids

# Create your models here.

class UserBid(models.Model):
    st_choise = (
        ("pending", "pending"),
        ("processing", "processing"),
        ("compelete", "compelete"),
    )
    owner = models.ForeignKey(Profile, verbose_name="profile", on_delete=models.CASCADE, null=True, blank=True)
    bid = models.ForeignKey(Bids, verbose_name="bid", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=200, choices=st_choise, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.owner) + "  "+ str(self.bid)

