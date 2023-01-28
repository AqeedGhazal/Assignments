from django.shortcuts import render , redirect 
from .models import user 
from users_app import models
def index(request):
    context = { 
    "users" : user.objects.all()
    }
    return render ( request,"index.html",context)


def create_user(request):
    if request.method == "POST":
        models.create_new_user(request)
        return redirect('results/')
    else:
        return redirect('/')

def results (request):
    context = { 
    "users" : user.objects.all()
    }
    return render (request ,"users.html" , context)