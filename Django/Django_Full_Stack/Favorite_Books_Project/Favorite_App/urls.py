from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index) , 
    path('register' , views.user_register),
    path('somepage', views.success_login),
    path('login' , views.user_login),
    path('logout' , views.user_logout),
    
]