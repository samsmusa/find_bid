from bid.models import UserBid
from user_login.models import Profile
from django.shortcuts import redirect, render, HttpResponse
from .forms import cutomUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    form = cutomUserForm()
    if request.method == "POST":
        form = cutomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bid:bids")

    context = {'form':form,}
    return render(request, 'user_login/signup.html', context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect('bid:bids')


    return render(request, 'user_login/login.html')


@login_required(login_url="user_login:login")
def logoutPage(request):
    logout(request)
    # messages.error(request, "User was Loged out")
    return redirect('user_login:login')


@login_required(login_url="user_login:login")
def ProfilePage(request):
    userprofile =  request.user.profile
    # userbid = UserBid.objects.filter(owner__name="samsmusa")
    userbid = userprofile.userbid_set.all()
    print(userbid)
    context = {"profile":userprofile, "userbid":userbid}
    return render(request, "user_login/profile.html", context)
