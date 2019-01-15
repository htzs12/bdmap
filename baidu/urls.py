from django.urls import path
from . import views

app_name = 'baidu'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('get_title/', views.get_title, name='get_title'),
    path('add_map/', views.add_map, name='add_map'),
    path('search_map/', views.search_map, name='search_map'),
    path('video/', views.video, name='video'),
]