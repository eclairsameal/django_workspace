from django.shortcuts import render
from .models import Project  # 導入Project 模組

# Create your views here.
def home(request):
    projects = Project.objects.all() # 從資料庫取得所有資料
    return render(request, 'portfolio/home.html', {"projects":projects})