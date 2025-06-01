from django.urls import path
from django.contrib.auth import views as auth_views
from . views import *


urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('accounts/profile/',profile, name='profile'),
    path('dashboard/',dashboard, name='dashboard'),
    path('register/',register,name='register'),
    path('login/', customlogin, name='customlogin'),
    path('logout/', customlogout, name='customlogout'),
]
