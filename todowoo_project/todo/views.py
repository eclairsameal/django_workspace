from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def sigunpuser(request):
    if request.method == 'GET':    # 檢查是否為GET方法
        return render(request, 'todo/sigunpuser.html', {'form':UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:    # 檢查密碼
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()    # 上面只是設定值，設定完後要用save存到資料庫裡
                login(request, user)    # 登入
                return redirect('currenttodos')    # 導向currenttodos(記得要return)
            except IntegrityError:    # 用戶名重複
                return render(request, 'todo/sigunpuser.html', {'form':UserCreationForm(),
                          'error':'That username has already been taken. Please choose a new username.'})
                
        else:
            # Tell the user the passwords didn't match
            return render(request, 'todo/sigunpuser.html', {'form':UserCreationForm(),
                          'error':'Passwords did not match'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')