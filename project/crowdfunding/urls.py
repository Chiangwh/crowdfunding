from django.urls import path,re_path
from . import views # Import the views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home, name = "home"),
    re_path(r'register',views.register, name ="register"),
    re_path(r'login',views.loginpage, name ="loginpage"),
    re_path(r'logout',views.logoutUser, name ="logout"),
    re_path(r'project',views.all_project_query,name="project"),
    re_path(r'create',views.createproject, name="createproject")
]

