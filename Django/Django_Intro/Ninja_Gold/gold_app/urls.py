from django.urls import path
from . import views

urlpatterns = [

    path('' , views.index), 
    path('gold/<location>', views.proccces_money),
    path('reset' , views.reset),

]