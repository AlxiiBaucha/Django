from django.shortcuts import render

def home(request):
    template_name = 'homepagge/home.html'
    return render(request, template_name)

def about(request):
    template_name = 'homepagge/about.html'
    return render(request, template_name)

def contact(request):
    template_name = 'homepagge/contact.html'
    return render(request, template_name)

def skills(request):
    context = {
        'skills': ['python', 'django', 'html', 'css']
    }
    template_name = 'homepagge/skills.html'
    return render(request, template_name, context)

