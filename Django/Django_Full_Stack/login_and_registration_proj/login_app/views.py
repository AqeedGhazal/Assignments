from django.shortcuts import render , redirect
from login_app import models
from .models import User , Message , Comment
import bcrypt
from django.contrib import messages


# Create your views here. # login_app

def index(request):
    return render (request , 'login.html')
def register_user(request):
    errors = User.objects.registervalidate(request.POST)
    if request.method == "POST" : 
        if len(errors)>0:
            for key , val in errors.items():
                messages.error(request , val)
            return redirect('/')
        else:
            models.creatuser(request)
    return redirect("/")

def success(request):
    if 'user_id' not in request.session:
        messages.error(request , "You must be logged in to view that page.")
        return redirect("/")
    else:
        context = {
            "user" : User.objects.get(id = request.session['user_id']),
            "all_messages":Message.objects.all()
        }
        return render (request , 'wall.html' , context)
def login(request):
    user_list = User.objects.filter(email=request.POST['login_email'])
    if len(user_list) == 0:
        messages.error(request, "Please check your email/password")
    if not bcrypt.checkpw(request.POST['login_password'].encode(), user_list[0].password.encode()):
        messages.error(request, "Please check your email/password")
        return redirect("/")
    request.session['user_id'] = user_list[0].id
    return redirect("/success")
def logout(request):
    request.session.flush()
    return redirect("/")

# the_wall_app 

def Create_Message(request):
    if request.method == "POST":
        models.create_new_msessage(request)
        return redirect("/success")

def Create_Comment(request):
    if request.method == "POST":
        models.create_new_comment(request)
        return redirect("/success")

def delete_comment(request , comment_id):
    Comment.objects.get(id = comment_id).delete()
    return redirect("/success")

