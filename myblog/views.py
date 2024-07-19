from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tour
from .form import ContactForm

# Create your views here.

def index(request):
    tours = Tour.objects.all()
    context = {"tours" : tours}
    return render(request, 'tours/index.html', context)

def home_view(request):
    return render(request, 'form_app/home.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
        

    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'form_app/contact.html', context)


def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')