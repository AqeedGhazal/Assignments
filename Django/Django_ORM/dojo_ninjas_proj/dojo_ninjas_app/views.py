from django.shortcuts import render , redirect 
from .models import Ninja , Dojo
from dojo_ninjas_app import models

# Create your views here.

def show(request):
    context = {
        "Dojos" : Dojo.objects.all()
        
    }
    return render (request ,'index.html' , context)

def create_Dojo(request):
    if request.method == "POST":
        models.create_new_Dojo(request)
        return redirect ('/')
        
def create_ninja(request):
    if request.method == "POST":
        models.create_new_ninja(request)
        return redirect('/')

def delete(request):
    if request.method == "POST":
        models.Delete_Dojo(request)
        return redirect('/')
