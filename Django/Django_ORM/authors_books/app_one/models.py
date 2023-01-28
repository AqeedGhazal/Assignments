from django.db import models
import datetime


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#this_authors = Author.objects.get(id=2) # get an instance of an Author 
#my_book = Book.objects.create(title = " Little Women" , author = this_authors)

class User (models.Model):
    firstname = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=65)
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)

class Appointments(models.Model):
    Taskname = models.TextField(max_length=255)
    Taskdate = models.DateTimeField(blank=True , null=True)
    Taskuser = models.ForeignKey(User , related_name='Appointments' ,  on_delete=models.DO_NOTHING)

def insertnewtask(request):
    Taskname = request.POST ['taskname']
    Taskdate = datetime.datetime.now()
    userid = 1
    Taskuser = User.objects.get(id=userid)
    Appointments.objects.create(Taskname = Taskname , Taskdate = Taskdate , Taskuser = Taskuser)