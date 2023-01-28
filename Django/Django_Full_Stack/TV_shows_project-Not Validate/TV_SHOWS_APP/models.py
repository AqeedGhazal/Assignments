from django.db import models 
from django.shortcuts import render


# Create your models here.

class Show(models.Model):
    Title = models.CharField(max_length=65)
    Network = models.CharField(max_length=65)
    Release_date = models.DateTimeField()
    desc = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Restful Routes : 
# Index , 

def index(request):
    context = { "shows" : Show.objects.all()}
    return render (request,'All_Shows.html',context)

def createshow(request):
    Title = request.POST['title']
    Network = request.POST['network']
    Release_date = request.POST['date']
    desc = request.POST['description']
    Show.objects.create(Title = Title , Network = Network , Release_date = Release_date , desc = desc)

def updateshow(request , show_id):
    show_to_edit = Show.objects.get(id=show_id)
    show_to_edit.Title = request.POST['title-1']
    show_to_edit.Network = request.POST['network-1']
    show_to_edit.Release_date = request.POST['date-1']
    show_to_edit.desc = request.POST['description-1']
    show_to_edit.save()

def deleteshow(request , show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
