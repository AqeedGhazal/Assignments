from django.shortcuts import render 
import random
# Create your views here.

def guess_number(request):
        guess_number = random.randrange(1,100)
        request.session ['guess'] = guess_number
        return render ( request , "index.html")
def check_value(request):
    if request.method == "POST":
        input_value = int(request.POST['input_guess'])
        random_guess = request.session['guess']

        if input_value > random_guess:
            context= {
            "box_color" : "red",
            "message" : "Too High ! "
            }
            return render(request , 'index.html' ,context  )
        elif input_value < random_guess :
            context = {
            "box_color" : "blue" ,
            "message" :  "Too low !"
            }
            return render(request , 'index.html' , context )
        else:
            context = {
            "box_color" : "green" , 
            "message" :f" Good Job ! ({random_guess}) was the number " ,
            #"message2" : f"you took {count} to get it right  "
            #"rest_buttn" : formatter('<a href="/"> <button type="submit">Play Again </button></a>' , filter_name='markdown')
            }
            del request.session['guess']
        return render (request , 'index.html' , context)


    