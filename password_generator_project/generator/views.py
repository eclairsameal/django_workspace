from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello there friend!")
    return render(request, 'generator/home.html')
    # return render(request, 'generator/home.html', {'password':'asdf456'})

def eggs(request):
    return HttpResponse("<h1>Eggs are so tasty</h1>")

def password(request):
    return render(request, 'generator/password.html')