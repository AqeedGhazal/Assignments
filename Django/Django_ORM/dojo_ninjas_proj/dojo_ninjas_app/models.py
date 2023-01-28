from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField( max_length = 45 , default= " old dojo")
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True  )

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_new_Dojo(request):
    name = request.POST ['name']
    city = request.POST ['city']
    state = request.POST ['state']

    Dojo.objects.create(name=name , city = city , state = state)

def create_new_ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    this_Dojo = Dojo.objects.get(id=request.POST['select_dojo'])


    Ninja.objects.create( first_name = first_name , last_name = last_name , Dojo = this_Dojo)

def Delete_Dojo(request):
    Dojo.objects.get(id=request.POST['delete']).delete()




