from django.urls import path
from . import views 

app_name = 'bid'

urlpatterns = [
    path('', views.bids, name='bids'),
    path('bid/<str:pk>', views.bid_details, name="bid_details"),
]
