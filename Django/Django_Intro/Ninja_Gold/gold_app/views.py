from django.shortcuts import render , redirect
from time import gmtime, strftime
import random


# Create your views here.

def index(request) :

    if 'gold' not in request.session:
        request.session['gold'] = 0

        request.session['full_str'] =''
        request.session['str_history'] = []
        request.session['date-time'] = ""
        request.session['time_stamp'] =[]
        request.session["text_color"] = ""
        request.session["color_history"] = []



    return render (request , 'index.html')

def proccces_money(request , location):
    earned_gold = 0 
    request.session['date-time'] = strftime("%Y/%m/%d %I:%M %p", gmtime())

    if 'count' not in request.session:
        request.session['count'] = 0
    if 'time_stamp' not in request.session:
        request.session['time_stamp'] = []
    
    if location == "farm":
        earned_gold = random.randint(10,20)  
        
    elif location == "cave":
        earned_gold = random.randint(5,10)
        
    elif location == "house":
        earned_gold = random.randint(2,5)
        
    elif location == "casino":
        earned_gold = random.randint(-50,50)
    request.session['count'] +=1
    request.session["gold"] += earned_gold

    if earned_gold > 0:
        request.session["full_str"] = 'Earned ' + str(earned_gold)+' golds from the '+location+'! '+'('+request.session["date-time"]+')'
        request.session["text_color"] = "green"

    if earned_gold == 0:
        request.session["full_str"] = 'Earned ' + str(earned_gold)+' golds from the '+location+'! '+'('+request.session["date-time"]+')'
        request.session["text_color"] = "black"

    elif earned_gold < 0:
        request.session["full_str"] = 'Entered a casino and lost '+str(earned_gold)+' golds... Ouch..! '+'('+request.session["date-time"]+')'
        request.session["text_color"] = "red"



    request.session["str_history"].append(request.session["full_str"])
    request.session["color_history"].append(request.session["text_color"])

    
    return redirect("/")

def reset(request):
    request.session.clear()

    return redirect("/")


