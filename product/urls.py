"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views


urlpatterns = [
    path('<id>', views.index, name='product-url'),
    path('api/<id>', views.read_product, name='read-product'),
    path('api/create/', views.create_product, name='create-product'),
    path('api/edit/<id>', views.update_product, name='update-product'),
    path('api/delete/<id>', views.delete_product,name='delete-product')
]
