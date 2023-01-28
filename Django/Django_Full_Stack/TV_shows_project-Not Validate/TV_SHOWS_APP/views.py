from django.shortcuts import render , redirect
from TV_SHOWS_APP import models
from .models import Show
# Create your views here.

def index(request):
    context = { "shows" : Show.objects.all()}
    return render (request,'All_Shows.html',context)


def newshow(request):
    return render (request , 'NewShow.html')

def Create_Show(request):
    if request.method == "POST":
        models.createshow(request)
        return redirect('/shows')

def viewshow(request , show_id):
    context = { "show" : Show.objects.get(id=show_id)}
    return render (request,'viewshow.html',context)

def edit_show(request , show_id):
    context = { "show" : Show.objects.get(id=show_id)}
    return render (request,'editshow.html',context)

def update_show(request , show_id):
    if request.method == "POST":
        models.updateshow(request , show_id)

    return redirect(f'/shows/{show_id}')

def Delete_show(request,show_id):
    models.deleteshow(request ,show_id)
    return redirect('/shows')
