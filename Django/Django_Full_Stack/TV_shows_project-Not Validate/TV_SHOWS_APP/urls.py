from django.urls import path , include
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new' , views.newshow),
    path ('new/createshow', views.Create_Show),
    path ('shows/<int:show_id>' , views.viewshow),
    path ('shows/<int:show_id>/edit' , views.edit_show),
    path ('shows/<int:show_id>/edit/update', views.update_show),
    path ('shows/<int:show_id>/delete' , views.Delete_show)
]