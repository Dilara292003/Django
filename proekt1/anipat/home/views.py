from django.shortcuts import render
from .models import Service

def home(request):
    ser = Service.objects.all()
    context = {'home': ser}
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")


def service(request):
    return render(request, "home/service.html")

def contact(request):
    return render(request, "home/contact.html")
