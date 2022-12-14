"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),  # name提供給html引用
    path('eggs', views.eggs),
    # path('password/', views.password), # 結尾的斜線是一種偏好，有結束的感覺
    path('generatedpassword/', views.password, name='password')
]
