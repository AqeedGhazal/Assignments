from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , redirect
from . import models
import bcrypt
from .models import User , Engineer , Company , Product , Review ,AltProduct
from django.contrib import messages


# Create your views here.

def mainpage(request):
    return render(request , 'Mainpage.html')

def Log_reg (request):
    return render (request , 'Login&reg.html')

def register_user(request):
    errors = User.objects.user_validator(request.POST)
    if request.method == 'POST':
        if len(errors) >0 : 
            for key, value in errors.items():
                messages.error(request ,value)
                return redirect('/reg')
        else:
            user = request.POST
            password =user['regesterd-C-userpassword']
            PW_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            models.create_user(user['firstname'] ,user['lastname'] , user['email'] , PW_hash )
            return redirect('/reg')

def register_engineer(request):
    errors = Engineer.objects.Engineer_validator(request.POST)
    if request.method == 'POST':
        if len(errors) >0 : 
            for key, value in errors.items():
                messages.error(request ,value)
                return redirect('/reg')
        else:
            engineer = request.POST
            password =engineer['regesterd-engpassword']
            PW_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            models.create_engineer(engineer['firstname'] ,engineer['lastname'] , engineer['email'] ,engineer['PhoneNumber'], PW_hash )
            return redirect('/reg')

def login_user(request):
    errors = User.objects.login_validator(request.POST)
    if request.method == 'POST':
        if len(errors) >0 :
            for key, value in errors.items():
                messages.error(request ,value)
                return redirect('/reg')
        else:
            users_list = models.get_users_list(request.POST['emailuser'])
            if len (users_list) == 0 :
                messages.error(request , 'please check your Email/Password')
            if not bcrypt.checkpw(request.POST['passworduser'].encode() , users_list[0].password.encode()):
                messages.error(request , 'please check your password')
                return redirect('/reg')        
            request.session['user_id'] = users_list[0].id
            return redirect('/allproducts') # redirect the user to products page . 

def login_engineer(request):
    errors = Engineer.objects.login_validator(request.POST)
    if request.method == 'POST':
        if len(errors) >0 :
            for key, value in errors.items():
                messages.error(request ,value)
                return redirect('/reg')
        else:
            engineers_list = models.get_engineers_list(request.POST['email'])
            if len (engineers_list) == 0 :
                messages.error(request , 'please check your Email/Password')
            if not bcrypt.checkpw(request.POST['password'].encode() , engineers_list[0].password.encode()):
                messages.error(request , 'please check your password')
                return redirect('/reg')        
            request.session['engineer_id'] = engineers_list[0].id
            return redirect('/products') # redirect the engineer to his page . 

def success_login_user(request ):
    if 'user_id' not in request.session:
        messages.error(request ,'You must login to view that page')
        return redirect('/reg')
    else:
        context = {
            "user": models.get_user_id(request.session['user_id']),
            "products": Product.objects.all(),
            #"engineer" : models.get_engineer_id(request.session['engineer_id'])

        }
        return render(request ,'products.html', context )

def success_login_eng(request):
    if 'engineer_id' not in request.session:
        messages.error(request , 'You Must login to view that page')
        return redirect('/reg')
    else:
        context = {
            "engineer": models.get_engineer_id(request.session['engineer_id'])
        }
    return render(request , 'add_products.html' , context)


def create_product(request):
    errors = Product.objects.Product_Validator(request.POST)
    if request.method == "POST":
        if len(errors)>0 :
            for key , value in errors.items():
                messages.error(request , value)
            return redirect('/products')
        else:
            if len(models.get_number_productexist(request.POST["title"]))> 0 :
                product = Product.objects.get(Title = request.POST['title'])
            else:
                uploaded_by = Engineer.objects.get(id=request.session['engineer_id'])

                product = request.POST
                models.createproduct(product['title'] , product['desc'] , product['usedfor'] , product['advantages'] , uploaded_by)
                productt=models.get_product(product['title'])
                if len(models.get_number_companyexist(request.POST['new-company']))< 1:
                    models.creat_company(request.POST['new-company'])
                    Company = models.get_company(request.POST['new-company'])
                    productt.company.add(Company)
                else :
                    Company = models.get_company(request.POST['exist-company'])
                    productt.company.add(Company)
            return redirect('/products')


def logout_user(request):
    request.session.clear()
    return redirect("/reg")


def showproductseng(request):
    context = {
            "engineer": models.get_engineer_id(request.session['engineer_id']),
            "products": Product.objects.all(),
            "company" : Company.objects.all(),
        }
    return render(request , 'products_eng.html' , context)

def show_product(request , product_id ):
    context = {
        #"user":User.objects.get(id=request.session['user_id']),
        "product" : Product.objects.get(id = product_id),
        
        "engineer" : models.get_engineer_id(request.session['engineer_id']),
        "alt_product":AltProduct.objects.all(),
        "reviews" : Product.objects.get(id=product_id).product_reviews.all(),
        "alt_product" : Product.objects.get(id=product_id).alt_products.all(),

    }
    return render (request , 'productdetails.html' , context)

def show_product_user(request , product_id ,):
    context = {
        "user":User.objects.get(id=request.session['user_id']),
        "product" : Product.objects.get(id = product_id),
        #"engineer" : models.get_engineer_id(request.session['engineer_id']),
        "alt_product":Product.objects.get(id = product_id).alt_products.all(),
        "reviews" : Product.objects.get(id=product_id).product_reviews.all() 

    }
    return render (request , 'productdetailsuser.html' , context)

def create_altr_product(request , product_id):
    uploaded_by = Engineer.objects.get(id=request.session['engineer_id'])
    product = request.POST
    productt = Product.objects.get(id = product_id)
    models.create_alt_product(product['alt-title'] , product['alt-desc'] , product['alt-usedfor'] , product['alt-advantages'] , uploaded_by , productt)
    return redirect('/products')

def delete_altr_product(request , altr_product_id ,product_id):

    altr_product = AltProduct.objects.get(id=altr_product_id)
    altr_product.delete()
    return redirect(f'/showproduct/{product_id}')

def user_addreview(request , product_id):
    user = User.objects.get(id = request.session['user_id'])
    product = Product.objects.get(id=product_id)
    Review.objects.create(rating=request.POST['rating'] , review = request.POST['review'] , user = user , product = product)
    return redirect(f"/showproductuser/{product.id}")

def user_deletereview(request , review_id , product_id):

    review =Review.objects.get(id=review_id)
    review.delete()
    return redirect (f'/showproductuser/{product_id}')

def engineer_info(request , engineer_id):
    context = {
        "engineer" : Engineer.objects.get(id = engineer_id),
        "engineer_products" : Engineer.objects.get(id=engineer_id).product_uploaded.all()
    }
    return render(request , 'engineer_info.html' , context)

def eng_addreview(request , product_id):
    engineer = Engineer.objects.get(id = request.session['engineer_id'])
    product = Product.objects.get(id=product_id)
    Review.objects.create(rating=request.POST['rating'] , review = request.POST['review'] , engineer = engineer , product = product)
    return redirect(f"/showproduct/{product.id}")
