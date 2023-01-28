from django.db import models

# Create your models here.
class Movie(models.Model): # Movie is inherit from (models.Model)
    title = models.CharField(max_length=45)
    descreption = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "Title: {}".format(self.title)