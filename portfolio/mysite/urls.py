from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='home'),
    path('project', views.project, name='project'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
