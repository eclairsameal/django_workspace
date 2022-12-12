from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sigunpuser(request):
    return render(request, 'todo/sigunpuser.html', {'form':UserCreationForm()})
