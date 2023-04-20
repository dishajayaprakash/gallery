from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser, CustomUserManager

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email','')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            # Passwords match, create user
            user = CustomUser.objects.create_user(username=username, email=email, password=password1)
            user.save()
            
            
            # Log in the user
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('gallery')
        else:
            # Passwords don't match, show error message
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'register.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser, CustomUserManager

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if a user with the provided email or username exists in the database
        if '@' in email:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                user = None
        else:
            try:
                user = CustomUser.objects.get(username=email)
            except CustomUser.DoesNotExist:
                user = None

        # If the user exists and the password is correct, log in the user
        if user is not None and user.check_password(password):
            authenticate(request, email=user.email, password=password)
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('gallery')
        else:
            error_message = 'Invalid email or password. Please try again.'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})


