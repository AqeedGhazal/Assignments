from django.db import models
import re
from datetime import datetime # insert datetime 
# Create your models here.

class Usermanger(models.Manager):
    def reg_validator(self , postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (len(postData['first_name']) == 0 or
            len(postData['last_name']) == 0 or
            len(postData['email']) == 0 or
            len(postData['password']) == 0 or 
            len(postData['confirmation_password']) == 0):
            errors['empty_field'] = "All fields must be completed for registration."
        
        if len(postData['first_name']) < 2 :
            errors['first_name'] = "Name has ti be at least 2 characters ."
        if len(postData['last_name']) < 2 :
            errors['last_name'] = "Alias has ti be at least 2 characters ."
        if len(postData['password']) < 8 :
            errors['password'] = "The password has to be at least 8 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if postData['password'] != postData['confirmation_password']:
            errors['password_no_match'] = 'Your passwords do not match.'
        #release_date = datetime.strptime(postData['date'], '%Y-%m-%d').date()
        #if release_date>= datetime.date(datetime.now()):
            #errors['date'] = "release_date must be in the past "
        return errors

    def login_validator(self , postData):
        errors = {}
        if (len(postData['login_email']) ==0):
            errors['login_email'] = "Email address should be filled" 
        if (len(postData['login_password']) ==0):
            errors['login_password'] = "Password address should be filled" 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):
            errors['email'] = "Invalid email address!"
        return errors





class User(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Usermanger()
    #books_uploaded = list of books uploaded by given user 
    #liked_books = list of books a given user liked


class Book(models.Model):
    title = models.CharField(max_length=65)
    desc = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User , related_name="books_uploaded" , on_delete=models.CASCADE)
    user_who_like = models.ManyToManyField(User , related_name="liked_books")


def create_user(first_name , last_name , email , password):
    return User.objects.create(first_name = first_name , last_name = last_name , email=email , password = password)

def get_users_list(email):
    return User.objects.filter(email=email)
