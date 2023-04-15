from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
# Create your views here.

def index(request):
    return render(request, 'index.html')



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
                
                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('register')
        else:
            messages.info(request ,'Password Not Correct!')
            return redirect('register')
        
    else:   
        return render(request, 'register.html')






def login(request):
    return render(request, 'login.html')