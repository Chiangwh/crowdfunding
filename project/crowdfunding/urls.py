from django.urls import path,re_path
from . import views # Import the views

urlpatterns = [
    path('',views.home, name = "home"),
    re_path(r'^register',views.register, name ="register"),
    re_path(r'^login',views.loginpage, name ="loginpage"),
    re_path(r'^logout',views.logoutUser, name ="logout"),
]