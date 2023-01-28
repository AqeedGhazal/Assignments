from django.db import models

# Create your models here.

from django.db import models
import re 
from datetime import date , datetime , time , timezone


# Create your models here.

class EngManger(models.Manager):
    def Engineer_validator(self , postData):
        errors = {}
        if len(postData['firstname']) < 2 : 
            errors['firstname'] = " first name should be at least 2 characters"
        if len(postData['lastname']) < 2 : 
            errors['lastname'] = " last name should be at least 2 characters"
        if len(postData['lastname']) < 2 : 
            errors['lastname'] = " last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):             
            errors['email'] = "Invalid email address!"
        if len(postData['regesterd-engpassword']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['regesterd-engpassword'] != postData['regesterd-c-engpassword']:
            errors['password_no_match'] = 'Your passwords do not match.'
        
        for E in Engineer.objects.all():
            if postData['email']==E.email:
                errors["DuplicateEmail"]="This Email is Used"
        return errors
    
    def login_validator(self , postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (len(postData['email']) ==0):
            errors['email'] = "Email address should be filled"
        if (len(postData['password']) ==0):
            errors['password'] = "Password should be filled" 
        
        return errors

class UserManger(models.Manager):
    def user_validator(self , postData):
        errors = {}
        if len(postData['firstname']) < 2 : 
            errors['firstname'] = " first name should be at least 2 characters"
        if len(postData['lastname']) < 2 : 
            errors['lastname'] = " last name should be at least 2 characters"
        if len(postData['lastname']) < 2 : 
            errors['lastname'] = " last name should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email address!"
        if len(postData['regesterd-userpassword']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['regesterd-userpassword']!=postData['regesterd-C-userpassword']:
            errors["password"] = "Password does not match"

        for E in User.objects.all():
            if postData['email']==E.email:
                errors["DuplicateEmail"]="This Email is Used"
        return errors
    
    def login_validator(self , postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (len(postData['emailuser']) ==0):
            errors['email'] = "Email address should be filled"
        if (len(postData['passworduser']) ==0):
            errors['password'] = "Password should be filled" 
        
        return errors

class ProductManger(models.Manager):
    def Product_Validator(self,PostData):
        errors = {}
        if len (PostData['title']) == 0 :
            errors['Title'] = "please fill the Product Title "
        
        return errors

class User(models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManger()

class Engineer (models.Model):
    First_Name = models.CharField(max_length=45)
    Last_Name = models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    image=models.ImageField(upload_to ='images' , null=True , blank=True)
    phoneNumber = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EngManger()


class Company(models.Model):
    Name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    Title = models.CharField(max_length=45)
    Description=models.TextField()
    used_for = models.TextField()
    Advantages = models.TextField()
    Datasheet = models.FileField(upload_to='files/')
    company = models.ManyToManyField(Company ,related_name="products")
    uploaded_by = models.ForeignKey(Engineer ,related_name='product_uploaded' , on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManger()

class AltProduct(models.Model):
    Title = models.CharField(max_length=45)
    Description=models.TextField()
    used_for = models.TextField()
    Advantages = models.TextField()
    Datasheet = models.FileField(upload_to='files/')
    product = models.ForeignKey(Product , related_name='alt_products' , on_delete=models.CASCADE , null=True)
    company = models.ManyToManyField(Company ,related_name="alt_products")
    uploaded_by = models.ForeignKey(Engineer ,related_name='alt_product_uploaded' , on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManger()

class Review(models.Model):
    rating = models.FloatField()
    review = models.TextField()
    user = models.ForeignKey(User, related_name='user_reviews' , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name ='product_reviews' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def create_user(First_Name , Last_Name , email , password):
    return User.objects.create(First_Name = First_Name , Last_Name=Last_Name , email=email , password = password)

def create_engineer(First_Name , Last_Name , email , password , phoneNumber ):
    return Engineer.objects.create(First_Name = First_Name , Last_Name = Last_Name , password = password , email=email , phoneNumber=phoneNumber)

def get_users_list(email):
    return User.objects.filter(email=email)
def get_engineers_list(email):
    return Engineer.objects.filter(email=email)
def get_user_id(id):
    return User.objects.get(id=id)
def get_engineer_id(id):
    return Engineer.objects.get(id=id)
def createproduct(Title , Description , used_for , Advantages , uploaded_by ):
    return Product.objects.create(Title = Title , Description=Description , used_for=used_for , Advantages=Advantages , uploaded_by=uploaded_by )

def create_company(Name):
    return Company.objects.create(Name=Name)

def get_number_productexist(Title):
    return Product.objects.filter(Title = Title)

def get_product(Title):
    return Product.objects.get(Title=Title)

def get_number_companyexist(Name):
    return Company.objects.filter(Name=Name)

def creat_company(Name):
    return Company.objects.create(Name=Name)
def get_company(Name):
    return Company.objects.get(Name=Name)

def create_alt_product(Title , Description ,used_for , Advantages , uploaded_by , product ):
        return AltProduct.objects.create(Title = Title , Description=Description , used_for=used_for , Advantages=Advantages , uploaded_by=uploaded_by , product=product )

def get_alt_product(Title):
    return AltProduct.objects.get(Title=Title)