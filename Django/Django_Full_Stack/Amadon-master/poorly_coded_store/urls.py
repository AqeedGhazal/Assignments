from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy', views.checkout),
    path ('checkout', views.checkout_view)
]
