from django.urls import path 
from. import views
from books_authors_app.models import Book , Author

urlpatterns = [
    path("" , views.show_book),
    path("createbook" , views.create_book),
    path('books/<int:book_id>',views.view_book),
    path('books/add_author' , views.add_author),
    path('authors' , views.show_author),
    path('addauthor', views.create_author),
    path('authors/<int:author_id>', views.view_author),
    path('author/add_book' , views.add_book),
    path('delete/<int:book_id>', views.delete_book),
    #path('delete/<int:author_id>' , views.delete_author)
]