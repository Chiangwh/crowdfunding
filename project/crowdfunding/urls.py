from django.urls import path,re_path
from . import views # Import the views

urlpatterns = [
    path('',views.login),
    re_path(r'register',views.register),
]