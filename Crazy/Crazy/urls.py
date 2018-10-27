"""Crazy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.acclogin, name='login'),
    path('web_ssh', views.web_ssh, name='web_ssh'),
    path('host_mgr/cmd', views.host_mgr, name='batch_cmd'),
    path('host_mgr/file_transfer', views.file_transfer, name='file_transfer'),
    path('batch_task_mgr', views.batch_task_mgr, name='batch_task_mgr'),
    path('task_result', views.task_result, name='get_task_result'),
    path('', views.test),
]
