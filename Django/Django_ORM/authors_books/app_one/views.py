from django.shortcuts import render , redirect
from app_one import models


# Create your views here.

def createtask(request):
    return render (request ,'task.html')

def createusertask(request):
    if request.method == "POST":
        models.insertnewtask(request)
        return redirect("/myaccount")
    else:
        return redirect ("/")