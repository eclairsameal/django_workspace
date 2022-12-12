from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def sigunpuser(request):
    if request.method == 'GET':    # 檢查是否為GET方法
        return render(request, 'todo/sigunpuser.html', {'form':UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password']:    # 檢查密碼
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()    # 上面只是設定值，設定完後要用save存到資料庫裡
        else:
            # Tell the user the passwords didn't match