from django.db import models
import bcrypt
import re

# Create your models here.


class UserManager(models.Manager):
    def registervalidate(self , postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (len(postData['first_name'])==0 or
        len(postData['last_name'])==0 or
        len(postData['registered_email']) == 0 or 
        len(postData['registered_password']) == 0):
            errors ['empty_field'] = "All fields must be completed for registration."
        
        if (len(postData['first_name'])) < 2 :
            errors['first_name_error'] = 'The first name has to be at least 2 characters.'
        if (len(postData['last_name'])) < 2 :
            errors['last_name_error'] = 'The Last name has to be at least 2 characters.'
        if not EMAIL_REGEX.match(postData['registered_email']):
            errors['rigistered_email'] = "Invalid Email Address"
        if postData['registered_password'] != postData['registered_confirm_pw']:
            errors['password'] = "your password has no match"
        if (len(postData['last_name'])) <= 8 :
            errors['password_short'] = "the password has to be at least 8 characters"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    User = models.ForeignKey(User , related_name='messages' , on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    User = models.ForeignKey(User , related_name="comments" , on_delete=models.DO_NOTHING)
    Message = models.ForeignKey(Message , related_name="comments" , on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def creatuser(request):
    
        password = request.POST['registered_password']
        pw_hash = bcrypt.hashpw(password.encode() , bcrypt.gensalt()).decode()


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['registered_email']
        password = pw_hash

        created_user = User.objects.create(first_name =first_name , last_name = last_name , email = email , password = pw_hash)
    
        request.session['user_id'] = created_user.id

# Wall_App 

def create_new_msessage(request):
    message = request.POST['new_message']
    this_user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(message=message , User = this_user)

def create_new_comment(request):
    comment = request.POST['new_comment']
    this_user = User.objects.get(id = request.session['user_id'])
    this_message = Message.objects.get(id=request.POST['msg_id'])
    Comment.objects.create(comment=comment , User=this_user , Message=this_message)