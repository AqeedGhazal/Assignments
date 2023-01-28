from django.urls import path
from . import views
urlpatterns = [
    path('bears/<str:name>',views.root_method),
    path('another_route',views.another_method),
    path('redirected_route',views.redirected_method),
]