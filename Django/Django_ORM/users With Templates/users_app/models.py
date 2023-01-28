from django.db import models

class user(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name = models.CharField(max_length= 255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_new_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email']
    age = request.POST['age']
    
    user.objects.create(first_name = first_name , last_name = last_name , email_address = email_address , age = age)
