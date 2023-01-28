from django.shortcuts import render ,redirect
from .models import Book , Author
from books_authors_app import models


# Create your views here.

def show_book(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request ,'book.html' ,context)

def create_book(request):
    if request.method == "POST":
        models.createbook(request)
        return redirect("/")

def view_book(request , book_id ):
    context={
        "book":Book.objects.get(id=book_id),
        "authors":Author.objects.all()
    }
    return render(request ,'bookview.html' , context)

def delete_book(request , book_id):

        models.deletebook(request , book_id)
        return redirect("/")

def add_author(request): # add author 
    if request.method == "POST":
        models.addauthor(request)
        return redirect(f"/books/{request.POST['book_id']}")

def create_author(request):
    if request.method =="POST":
        models.createauthor(request)
        return redirect("/authors")

def show_author(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request , 'author.html' , context)


def view_author(request , author_id ):
    context={
        "book":Book.objects.all(),
        "authors":Author.objects.get(id=author_id)
    }
    return render(request ,'authorview.html' , context)

def add_book(request):
    if request.method == "POST":
        models.addbook(request)
        return redirect(f"/authors/{request.POST['author_id']}")

#def delete_author(request , author_id):
    #models.deleteauthor(request , author_id)
    #return redirect("/authors")





