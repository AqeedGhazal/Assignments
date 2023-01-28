from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.display),
    path('destroy/',views.destroy),
    path('count/' , views.count)
]