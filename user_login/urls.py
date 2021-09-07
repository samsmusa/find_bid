from django.urls import path
from user_login import views

app_name = 'user_login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginUser, name='login' ),
    path('logout/', views.logoutPage, name='logout'),
    path('profile/', views.ProfilePage, name="profile"),
]
