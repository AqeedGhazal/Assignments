from django.shortcuts import render
from time import gmtime ,strftime 
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M %p")
    context = {
    "date" : strftime("%b %d, %Y"),
    "time" : timestamp

    }
    return render (request , 'time_display.html ' , context )