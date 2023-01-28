from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse

# Create your views here.

def index(request  ,name): # function called index 
    return HttpResponse("this is the equivlent of @app.route('/') !")

def root_method(request,name):
    return HttpResponse("string response from root method")

def another_method(reauest):
    return redirect("/redirected_route")

def redirected_method(request):
    return JsonResponse({"name":"John", "age":30, "car":'BM' })