from django.contrib import admin
from django.urls import path
from . import views

app_name = 'baidu'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('get_title/', views.get_title,name='get_title'),
]