from django.shortcuts import render

# Create your views here.
def login(request): #Renders 'crowdfunding/login.html'template
    return render(request,'crowdfunding/login.html')

def register(request): #Renders 'crowdfunding/register.html'template
    return render(request,'crowdfunding/register.html')