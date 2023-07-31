from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def index_view(request):
    return render(request, 'mysite/index.html')


def about_view(request):
    return render(request, 'mysite/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'mysite/contact.html', {'form':form})
