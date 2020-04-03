from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "welcome.html")


def contact(request):
    return render(request, "contact.html")


def details(request):
    return render(request, "details.html")


def functions(request):
    return render(request, "functions.html")


def apperance(request):
    return render(request, "apperance.html")


def pricing(request):
    return render(request, "pricing.html")

