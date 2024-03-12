from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from transactions.models import Transaction

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        print("User is authenticated")
        # Retrieve the latest 4 transactions for the current user
        latest_transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:4]
        
        # Now you have access to the latest 4 transactions related to the logged-in user
        
        context = {
            'latest_transactions': latest_transactions,
        }
        return render(request, 'home.html',context)
    else:
        return render(request, 'home.html')

def register(request):
    # print("Login")
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        # confirm_password=password
        
        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,first_name=fname,last_name=lname)
                user.save()
                messages.success(request, f'You have successfully registered: {user.username}')
                return redirect('home')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'You have successfully logged-in: {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            print("Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

