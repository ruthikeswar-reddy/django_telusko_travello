from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if password1 == password2:
            if User.objects.filter(username= username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'This Email is already used to register')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password1, first_name=first_name, last_name= last_name,email=email )
                user.save()
                print('user is successfully created')
                return redirect('login')
        else:
            messages.info(request, 'recheck your password and fill the details again')
            return redirect('register')
            
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password= password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "user is not found, try again and check your credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')