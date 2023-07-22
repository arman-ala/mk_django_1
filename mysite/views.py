from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse("<h1> This is Home Page </h1>")


def about_view(request):
    return HttpResponse("<h1> This is About Page </h1>")


def contact_view(request):
    return HttpResponse("<h1> This is Contact Page </h1>")
