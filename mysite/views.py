from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm, NewsletterForm


def index_view(request):
    return render(request, 'mysite/index.html')


def about_view(request):
    return render(request, 'mysite/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didn\'t submit successfully!')
    form = ContactForm()
    return render(request, 'mysite/contact.html', {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(data = request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')
