from django.contrib import admin
from django.urls import path 
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index), # show the form 
    path("create" , views.register_user), # create the user / rigister the user , handling post request then redirect . 
    path('success' , views.success), # 
    path('login' , views.login),
    path('logout' , views.logout),
    path('addmessage', views.Create_Message),
    path('addcomment' , views.Create_Comment),
    path('comment/<int:comment_id>/delete' , views.delete_comment)

]
