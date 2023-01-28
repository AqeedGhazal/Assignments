from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.index),
    path('addcourse' ,views.create_course ),
    path('courses/destroy/<int:course_id>', views.confirm_delete),
    path('courses/destroy/<int:course_id>/delete' , views.destroy_course)
]
