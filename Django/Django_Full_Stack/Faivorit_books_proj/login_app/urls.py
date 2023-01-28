from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.showpage), # view the login/ registration form 
    path('register' , views.register_user) , # create new user 
    path('login' , views.login_user), # handle the login form 
    path('books' , views.success_login), # view the books html page . 
    path('logout' , views.logout),
    path('books/addbook' , views.add_book),# Upload Book 
    path('books/<int:book_id>/add_fav', views.add_to_fav),
    path('books/<int:book_id>/remove_fav' , views.remove_from_fav),
    path('books/<int:book_id>', views.show_book),
    path('books/<int:book_id>/edit' , views.edit_book),
    path ('books/<int:book_id>/delete' , views.delete_book),

]
