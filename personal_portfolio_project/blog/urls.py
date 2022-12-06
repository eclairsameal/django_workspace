from django.urls import path, include
from . import views

app_name = 'blog'    # 指定應用程式名稱

urlpatterns = [
    path("", views.all_blogs, name="all_blogs"),
    path('<int:blog_id>/', views.detail, name='detail'),  # 會傳數字給views.detail
]

"""
    path("1", views.detail, name="detail"),
    path("2", views.detail, name="detail"),
    path("3", views.detail, name="detail"),
    * 注意 <int:blog_id> 分號兩邊不能有空白
"""