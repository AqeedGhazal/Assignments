from django.shortcuts import render , redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
from . import models




# Create your views here.

# 1- handel the registration methods / rules .

    # Function that render the login & rigestration page 
def showpage(request):
    
    return render (request ,'login_rige.html')

def register_user(request):

    errors = User.objects.user_validator(request.POST)
    if request.method == 'POST':
        if len(errors)> 0 : 
            for key , value in errors.items():
                messages.error(request, value)
            
            return redirect('/')
        else:

            user = request.POST 
            password=user['registered_password']
            PW_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            models.create_user(user['registered_first_name'] , user['registered_last_name'] , user['registered_email'] , PW_hash )

            return redirect('/')


# 2- handel the login methods / rules . 

def login_user(request):
    
    users_list = User.objects.filter(email= request.POST['login_email'])
    
    if len (users_list) == 0 :
        messages.error(request , 'please check your Email/Password')
    
    if not bcrypt.checkpw(request.POST['login_password'].encode() , users_list[0].password.encode()):
        
        messages.error(request , 'please check your password')
        
        return redirect('/')        
    request.session['user_id'] = users_list[0].id
        
    return redirect('/books')

def success_login(request):

    if 'user_id' not in request.session:
        messages.error(request ,'You must login to view that page')
        return redirect('/')
    else:
        context = {
            "user":User.objects.get(id = request.session['user_id']),
            "all_books": Book.objects.all(),
        }

        return render(request ,'favbooks.html', context )

def logout(request):
    request.session.clear()
    return redirect('/')


# books rules / 

def add_book(request): # here how we do the one to one relation . 
    errors = Book.objects.Book_validator(request.POST)
    if request.method == "POST":
        if len(errors)> 0 : 
            for key , value in errors.items():
                messages.error(request, value)
            
            return redirect('/books')
        else:
            book = request.POST
            uploaded_by = User.objects.get(id=request.session['user_id'])
            models.upload_book(book['title'] , book['descreption'] ,uploaded_by)
            return redirect('/books')


def add_to_fav(request, book_id): # here is how we do the many to many relation , 
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    user.liked_books.add(book)
    return redirect(f"/books/{book_id}")

def remove_from_fav(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)
    return redirect(f"/books/{book_id}")

def show_book(request , book_id):
    context = {
        "user":User.objects.get(id=request.session['user_id']),
        "book" : Book.objects.get (id = book_id),
    }
    return render (request , 'bookdetails.html' , context)

def edit_book(request , book_id):
    book = Book.objects.get(id=book_id)
    errors = Book.objects.Book_validator(request.POST)

    if len(errors)>0:
        for key , value in errors.items():
            messages.error(request , value)
        return redirect (f'/books/{book_id}')
    book.title = request.POST['title']
    book.desc = request.POST['descreption']
    book.save()
    return redirect (f'/books/{book_id}')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    
    return redirect (f'/books/{book_id}')
