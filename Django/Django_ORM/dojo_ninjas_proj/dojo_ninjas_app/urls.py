from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show),
    path ('createninja', views.create_ninja),
    path ('createdojo', views.create_Dojo),
    path ('delete', views.delete),
]