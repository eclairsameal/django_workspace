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
    if request.GET.get("uppercase"):
        char_list.extend('abcdefghijklmnopqrstuvwxyz'.upper())
    if request.GET.get("special"):
        char_list.extend(list('!@#$%^&*()'))
    if request.GET.get("numbers"):
        char_list.extend(map(str, list(range(10))))
    # length = 10
    length = int(request.GET.get('length', 12))    # 從home.html 中取 length
    thepassword = ""
    
    for char in range(length):
        thepassword += random.choice(char_list)
    
    return render(request, 'generator/password.html', {"password":thepassword})

