from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(null=True) 
    books = models.ManyToManyField(Book, related_name="Authores")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def createbook(request):
    title = request.POST["title"]
    desc = request.POST["description"]
    Book.objects.create(title=title , desc = desc)

def createauthor(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    notes = request.POST ["notes"]
    Author.objects.create(first_name = first_name , last_name = last_name , notes=notes)

def deletebook(request , id):
    book = Book.objects.get(id = id)
    book.delete()

def addauthor(request):
    this_book = Book.objects.get(id = request.POST["book_id"])
    this_author = Author.objects.get(id =request.POST["author_id"])
    this_book.Authores.add(this_author)

def addbook(request):
    this_book = Book.objects.get(id = request.POST["book_id"])
    this_author = Author.objects.get(id =request.POST["author_id"])
    this_author.books.add(this_book)

#def deleteauthor(request , id):
    #author = Author.objects.get(id = id)
    #author.delete()