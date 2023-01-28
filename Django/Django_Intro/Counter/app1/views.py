from django.shortcuts import render ,redirect

# Create your views here.
def display(request):
    if 'count' in request.session : 
        request.session['count'] += 1 
    else:
        request.session['count'] = 1

    return render(request, 'counter.html')

def count(request):
    if request.method == "POST":
        #if request.POST['b']== 'reset':
            #request.session['count'] = 0
        if request.POST['b']=='add':
            request.session['count']+=1 
        return redirect('/')

def destroy(request):
    del request.session['count']
    return redirect('/')
    