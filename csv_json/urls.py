"""csv_json URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from converter.views import index
from rest_framework.urlpatterns import format_suffix_patterns
from converter import views

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('json/', views.JSONdata.as_view()),
    path('admin/', admin.site.urls),
]
