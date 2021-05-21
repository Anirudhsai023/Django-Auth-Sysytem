from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'You have been logged in')
            return redirect('dashboard')

        else:
            messages.error(request,'Invalid credentials')
            return redirect('/')


    else:    
        return render(request,"authtemp/base.html")

def register(request): 
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        if(password == confirm_password):

            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already exists")
                return render(request,"authtemp/register.html")


            if User.objects.filter(email = email).exists():
                messages.error(request,"email already exists")
                return render(request,"authtemp/register.html")
            
            user = User.objects.create_user(
                username = username, 
                email = email,
                 password = password,
                 first_name = first_name,
                 last_name = last_name)
            user.save()
            messages.success(request,"Account created succesfully")
            return redirect('/')
        
    
        else:
            messages.error(request, "Password did not match")
            return render(request,"authtemp/register.html")
    
    
    else:
        return render(request,"authtemp/register.html")

@login_required(login_url='/')
def signout(request):
    logout(request)
    return render(request,"authtemp/signout.html")
    

@login_required(login_url='/')
def dashboard(request):
    return render(request,"authtemp/dashboard.html")
