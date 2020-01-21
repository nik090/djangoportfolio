from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import requests

# Create your views here.


def index(request):
    mapbox_access_token = 'pk.eyJ1IjoibmlrMDkwIiwiYSI6ImNrNW8ybjNobzAxaGczbnBpYWViZWhoY3IifQ.wWhW8kIbXm_CTf6V_WfWrg'
    return render(request, 'mysite/index.html', {'mapbox_access_token': mapbox_access_token})


def project(request):
    return render(request, 'mysite/project.html')


def about(request):
    return render(request, 'mysite/about.html')


def contact(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        message_r = request.POST.get('message')
        c = Contact(name=name_r, email=email_r, message=message_r)
        c.save()
        return render(request, 'mysite/contact.html')
    else:
        return render(request, 'mysite/contact.html')
