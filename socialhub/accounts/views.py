from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.http import HttpResponse


# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if not user:
            messages.error(request,"Invalid credentials")
        else:
            login(request,user)
            messages.success(request,"Login success")
            return redirect('home')
            
    else:
        form = LoginForm()
        return render(request,'accounts/login.html',{'form':form})
def logout(request):
    pass
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,'Data is invalid please check')
    else:
        form = RegisterForm()
        return render(request,'accounts/register.html',{'form':form})
def home(request):
    return HttpResponse("Home")