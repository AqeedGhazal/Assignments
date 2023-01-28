from django.urls import path 
from . import views 

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('' , views.Creat_user),  #get
    path('results', views.Show_info), #post
    path('succsess' , views.success)    #get
]
