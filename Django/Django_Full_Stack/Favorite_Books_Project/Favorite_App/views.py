from django.shortcuts import render , redirect
from . import models
import bcrypt
from .models import User , Book
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request , 'index.html')

def user_register(request):
    errors = User.objects.reg_validator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0 :
            for key , value in errors.items():
                messages.error(request , value)
                return redirect('/')
        else:
            user = request.POST
            password = user['password']
            PW_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            models.create_user(user['first_name'] , user['last_name'] , user['email'] , PW_hash)
            return redirect('/')

def success_login(request):
    if 'user_id' not in request.session:
        messages.error(request ,'You must login to view that page')
        return redirect('/')
    else:
        context = {
            # pass the informations you need to the login page to be disapled 
        }
        return render(request , 'somepage.html' , context)

def user_login(request):
    errors = User.objects.login_validator(request.POST)
    if request.method == 'POST':
        if len(errors) >0 :
            for key, valuee in errors.items():
                messages.error(request ,valuee)
                return redirect('/')
        else:
            users_list = models.get_users_list(request.POST['login_email'])
            if len(users_list)==0 :
                messages.error(request , "please check your Email/Password")
            if not bcrypt.checkpw(request.POST['login_password'].encode(), users_list[0].password.encode()):
                messages.error(request , "please check your password")
                return redirect('/')
            request.session['user_id'] = users_list[0].id
            return redirect('/ #somepage')
def user_logout(request):
    request.session.clear()
    return redirect('/')


    


