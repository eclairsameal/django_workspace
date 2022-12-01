from django.shortcuts import render
from django.http import HttpResponse
import  random

# Create your views here.

def home(request):
    # return HttpResponse("Hello there friend!")
    return render(request, 'generator/home.html')
    # return render(request, 'generator/home.html', {'password':'asdf456'})

def eggs(request):
    return HttpResponse("<h1>Eggs are so tasty</h1>")

def password(request):
    char_list = list('abcdefghijklmnopqrstuvwxyz')
    length = 10
    thepassword = ""
    
    for char in range(length):
        thepassword += random.choice(char_list)
    
    return render(request, 'generator/password.html', {"password":thepassword})

