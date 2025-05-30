from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path('about',about, name='about'),
    path("skill",skills,name="skills")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
