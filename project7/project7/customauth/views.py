from django.shortcuts import render,redirect
from django.contrib.auth import *
from django.http import HttpResponse
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# @login_required(login_url='login')
# def profile(request):
    # if not request.user.is_authenticated:
    #     return HttpResponse("Please login first.")


    # context={
    #     'key':"554545"
    # }
    # return render(request,"customauth/profile.html",context)
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        messages.sucess(request,'Account created! you can now login')
        return redirect('login')
    return render(request, 'customauth/register.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'customauth/dashboard.html')

def customlogin(request):
    form = CustomLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            form.add_error(None, "Invalid credentials")

    return render(request, 'customauth/customlogin.html', {'form': form})

def customlogout(request):
    logout(request)
    return redirect('customlogin')