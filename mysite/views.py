from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'mysite/index.html')


def about_view(request):
    return render(request, 'mysite/about.html')


def contact_view(request):
    return render(request, 'mysite/contact.html')
