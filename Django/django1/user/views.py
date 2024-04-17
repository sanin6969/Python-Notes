from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
# Create your views here.
def login(request):
    error_message=None
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            print(user)
        else:
            error_message='invalid user'
    return render(request,'users/login.html',{'error_message':error_message})

def signup(request):
    user=None
    error_message=None
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e :
            error_message=str(e)   
    return render(request,'users/create.html',{'user':user,'error_message':error_message})
