from django.urls import path
from . import views

app_name = 'vue'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.TestView.as_view(), name='api'),
    path('api_auth/', views.TestAuthView.as_view(), name='api_auth'),
]