from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from . models import *
# Create your views here

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = CreateUserForm()
    return render(request,'reg.html',{'form':form})

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invaild details')
            return redirect('log_in')
    else:
        return render(request,"login.html")



def logout(request):
    auth.logout(request)
    return redirect('log_in')

# def register(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username is already taken")
#                 return redirect("register")
#
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email is already taken")
#                 return redirect("register")
#
#             else:
#                 user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
#                 user.save()
#                 print("user created")
#         else:
#             print("password not correct")
#             return redirect('register')
#
#         return redirect('/')
#
#     else:
#
#         return render(request,'reg.html')
#
# def login(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'invaild details')
#             return redirect('login')
#     else:
#         return render(request,"login.html")
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')



