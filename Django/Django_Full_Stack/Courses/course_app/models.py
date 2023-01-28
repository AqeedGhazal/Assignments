from django.db import models

# Create your models here.


class CourseManger(models.Manager):
    def Course_validate(self , postData):
        errors = {}
        if len(postData["name"]) == 0 or len(postData["descreption"]) == 0 :
            errors["empty_field"] = "All fields have to be filled out."
        if len(postData['name']) < 5 :
            errors['name'] = "Course Name must be at least 5 characters"
        if len (postData['descreption']) < 15 : 
            errors['descreption'] = "Course Descreption must be at least 15 characters"
        return errors

class Course(models.Model):
    Name = models.CharField(max_length=100)
    Discreption = models.TextField()
    objects = CourseManger()

    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

class Deiscreption (models.Model):
    Deiscreption = models.TextField()
    course = models.OneToOneField(Course , on_delete=models.CASCADE)

def addcourse(request):
    Name = request.POST['name']
    Descreption = request.POST['descreption']
    Course.objects.create(Name = Name , Discreption =Descreption)

def delete_course(request , course_id):
    course_to_delete =Course.objects.get(id = course_id)
    course_to_delete.delete()


