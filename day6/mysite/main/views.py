
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def home(request):
    template_name = 'main/home.html'
    return render(request, template_name)

def about(request):
    template_name = 'main/about.html'
    return render(request, template_name)

def contact(request):
    template_name = 'main/contact.html'
    return render(request, template_name)

def skills(request):
    context = {
        'skills': ['python', 'django', 'html', 'css']
    }
    template_name = 'main/skills.html'
    return render(request, template_name, context)

# def project(request):
#     template_name= 'main/project.html'
#     return render(request, template_name,)

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse("Thanks for contacting us!")
    return render(request, "contact.html")

def project(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'main/project.html', {'projects': projects})

def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    print(project)
    return render(request, 'main/project_detail.html', {'projects': project})