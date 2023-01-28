from django.shortcuts import render , redirect

# Create your views here.
def Creat_user(request):
    #if request.method == "GET": we dont need to put this , the default is get ???! 

    return render(request ,"form.html")

def Show_info(request):
    #if request.method == "POST":
        #x = request.session #  used session to solve the issue of not showing data 
        y = request.POST
        name = y ['name'] 
        location= y['location']
        language =  y['language'] 
        comments =  y['comments']

        context = {
            'name': name , 
            'location' : location ,
            'language' : language , 
            'comments' : comments ,
        }
        return redirect('/succsess' )

def success(request):
    return render(request , 'result.html')

    