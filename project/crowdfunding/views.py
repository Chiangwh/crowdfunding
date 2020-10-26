from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm

@login_required(login_url='loginpage') #send user back to login page if not login
def home(request): #Renders 'crowdfunding/home.html'template 
    return render(request,'crowdfunding/home.html')

def loginpage(request): #Renders 'crowdfunding/login.html'template 
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
             login(request, user)
             return redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect')
            

    context = {}
    return render(request,'crowdfunding/login.html',context)

def logoutUser(request):  #logout view, sending user back to login page
    logout(request)
    return redirect('loginpage')

def register(request): #Renders 'crowdfunding/register.html'template
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect ('crowdfunding/login.html')

    context = {'form':form}
    return render(request,'crowdfunding/register.html',context)