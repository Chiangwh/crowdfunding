from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2']

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['p_name','description','category']