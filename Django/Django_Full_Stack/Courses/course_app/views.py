from django.shortcuts import render , redirect
from .models import Course
from course_app import models
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request , 'AllCourse.html' , context)

def create_course(request):
    errors =Course.objects.Course_validate(request.POST)
    if request.method == 'POST':
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            models.addcourse(request)
    return redirect('/')

def confirm_delete(request , course_id):
    context = {
    "course" : Course.objects.get(id = course_id)
    }
    return render (request , 'delete.html' , context)

def destroy_course(request , course_id):
    models.delete_course(request , course_id)
    return redirect ('/')

