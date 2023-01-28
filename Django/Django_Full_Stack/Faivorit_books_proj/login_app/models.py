from django.db import models
import re
import bcrypt



# Create your models here.

class UserManger(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if (len(postData['registered_first_name']) == 0 or
            len(postData['registered_last_name']) == 0 or
            len(postData['registered_email']) == 0 or
            len(postData['registered_password']) == 0):
            errors['empty_field'] = "All fields must be completed for registration."

        if len(postData['registered_first_name']) < 2:
            errors['first_name_error'] = 'The first name has to be at least 2 characters.'
        if len(postData['registered_last_name']) < 2:
            errors['last_name_error'] = 'The last name has to be at least 2 characters.'
        if not EMAIL_REGEX.match(postData['registered_email']):         
            errors['email'] = "Invalid email address!"
        if postData['registered_password'] != postData['registered_confirm_pw']:
            errors['password_no_match'] = 'Your passwords do not match.'
        if len(postData['registered_password']) < 8:
            errors['short_password'] = 'The password has to be at least 8 characters.'
            
        return errors

class BookManager(models.Manager):
    def Book_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = 'Please fill out the title field.'
        if len(postData['descreption']) < 5:
            errors['descreption'] = 'Description has to be at least 5 characters long.'
        
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True )

    # book_uploaded = List of uploaded books by a given user ! 
    # liked_books = List of books a given user liked . 

    objects = UserManger()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    
    uploaded_by = models.ForeignKey(User , related_name='book_uploaded' , on_delete=models.CASCADE)

    # the user who uploaded a given book 

    # One is  a one-to-many relationship because a user can upload many books, and a book can be uploaded by one user. In our database, the uploaded_by_id field 
    # (in the books table) stores this relationship. 

    users_who_like = models.ManyToManyField(User , related_name='liked_books')

    # a list of users who like a given book . 

    #The second relationship is a many-to-many relationship, where a given user can like many books, and a given book can be liked by many users.
    # This relationship is stored in the third table. (In the diagram, this is the likes table.)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True )

    objects = BookManager()

#To get the user who uploaded a book: Book.objects.first().uploaded_by
#To get the list of books uploaded by a user: User.objects.first().books_uploaded.all()
#To get the list of users who like a book: Book.objects.first().users_who_like.all()
#To get the list of books a user likes: User.objects.first().liked_books.all()

# Function that handel createing a new user : 

def create_user(first_name , last_name , email , password):

    created_user = User.objects.create(first_name = first_name , last_name = last_name , email = email , password =password)

    #request.sesssion['user_id'] = created_user.id

# Functions that handel login the user : 

def upload_book(title , desc , uploaded_by):

    Book.objects.create(title=title ,desc=desc , uploaded_by=uploaded_by)

