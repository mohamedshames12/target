from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.

# this is functionality to allow you to go index page

def index(request):
    return render(request, 'index.html')

# this is functionality to allow you to go settings page
@login_required(login_url='settings')
def settings(request):
    return render(request, 'settings.html')

# I created a database connection to register
def register(request):
    
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['confirm-password']

        if password == con_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request,user_login)
                
                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request ,'Pass    word Not Correct!')
            return redirect('register')
        
    else:   
        return render(request, 'register.html')

# I created a database connection to login
def login(request):
    
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

# I created a database connection to logout
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')