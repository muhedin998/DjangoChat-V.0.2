# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('register/reg/',views.register,name='register'),
    path('login/log/',views.loginPage,name='login'),   
    path('login/logout/',views.logoutPage,name='logout')
]