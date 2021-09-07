from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from user_login.models import Profile
from .utils import SearchBids
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from user_login.models import Bids
from .forms import PlaceBid
from .models import UserBid

# Create your views here.
page = 'general'
def bids(request):
    # profiles = Profile.objects.all()
    # bid_list, search_query = SearchBids(request) 
    # result = 10
    # page = request.GET.get('page')
    # paginator = Paginator(bid_list, result)
    # try:
    #     bids_list = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     bids_list = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     bids_list = paginator.page(page)
    bids_list = Bids.objects.all()



    context = {'bids_list':bids_list,}
    return render(request, 'index.html', context)

def bid_details(request, pk):
    bid = Bids.objects.get(id=pk)
    
    try:
        profile= request.user.profile
        userbid = profile.userbid_set.get(bid__id=pk)
    except:
        userbid = None
    form = ''
    message = None
    if userbid is not None:
        message = "You al-ready bid this item!"
    else:
        form = PlaceBid()
        if request.method == "POST":
            form = PlaceBid(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.owner = request.user.profile
                obj.bid = bid
                obj.save()
                return redirect("bid:bids")
    context = {"bid":bid, "form":form, "message":message, "userbid":userbid}
    return render(request, "bid/bid_details.html", context)