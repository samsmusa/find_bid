from user_login.models import Bids
from django.db.models import Q

def SearchBids(request):
    bids_list = Bids.objects.all()
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        # tag = Bids.objects.filter(title__icontains=search_query)
        # profile = Profile.objects.filter(name__icontains=search_query)
        bids_list = Bids.objects.distinct().filter(
            Q(title__icontains=search_query) |
            Q(state__icontains=search_query) 
            # Q(owner__name__icontains=search_query)
            # Q(owner__in =profile)

        )
        print(bids_list.count())
    return bids_list, search_query