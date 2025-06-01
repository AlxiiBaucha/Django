
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    template_name = 'main/home.html'
    return render(request, template_name)

def about(request):
    template_name = 'main/about.html'
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

# def contact(request):
#     template_name = 'main/contact.html'
#     return render(request, template_name)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        return render(request, 'main/thankyou.html')
    context={
        "form":form
    }
    template_name="main/contact.html"
    return render(request, template_name,context)


def project(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'main/project.html', {'projects': projects})

def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    print(project)
    return render(request, 'main/project_detail.html', {'projects': project})

def form(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'main/thankyou.html')

    context={
        "form":form
    }
    template_name="main/forms.html"
    return render(request, template_name,context)

# def feedback(request):
#     form=FeedbackForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return render(request,'main/thankypu.html')
    
#     context={
#         "form":form
#     }
#     template_name="main/feedback.html"
#     return render(request, template_name,context)
    
def show_feedback(request):
    feeds=Feedback.objects.all()
    context={
        "form":feeds
    }
    return render(request,'main/feedback.html',context)

def show_form(request):
    feeds=Contact.objects.all()
    context={
        "form":feeds
    }
    return render(request,'main/showall.html',context)