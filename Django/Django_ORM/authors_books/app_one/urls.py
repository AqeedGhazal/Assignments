from django.urls import path , include
from. import views

urlpatterns = [
    path('createtask' , views.createtask),
    path('createusertask' , views.createusertask)
]