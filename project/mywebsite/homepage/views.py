from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    template_name = "homepage/home.html"
    return render(request,template_name)
def index(request):
    context = {
        "page_title": "Django Day 2",
        "message": "Welcome to Day 2 of DJANGO!"
    }
    return render(request, 'homepage/home.html', context)
# def index(request):
    # return HttpResponse("<h1 style='color: blue;font-family:courier;text-align:center;margin-top:50px;'>Day 2 Challenge Completed</h1>")
def about(request):
    return HttpResponse('<h1 style="color: blue;">Day 1 Challenge Completed</h1>')
