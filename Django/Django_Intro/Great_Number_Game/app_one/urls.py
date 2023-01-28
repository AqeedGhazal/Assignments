from django.urls import path , include
from . import views

urlpatterns = [

    path('' , views.guess_number ),
    path ('check' , views.check_value)
]
