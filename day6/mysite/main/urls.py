from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('contact/', contact, name='contact'),
    path('project/',project, name='project'),
    path('project/<int:id>/', project_detail, name='projects'),
    path('form/', form ,name='forms'),
    path('feedback/', show_feedback, name='feedback'),
    path('formas/', show_form, name='form'),









]


# from django.urls import path

# from .views import home,hello,profile
# urlpatterns =[
#     path("", home, name="home"),
#     path("hello/<str:name>/", hello, name="hello"),
#     path("profile", profile, name="profile"),
# ]