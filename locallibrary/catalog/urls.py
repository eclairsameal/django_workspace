from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),    # 將調用一個視圖函數：views.index, 它是views.py文件中名為index() 的函數。
]