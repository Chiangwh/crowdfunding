from django.urls import path,re_path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.debug import default_urlconf 
from . import views

urlpatterns = [
    path('',views.allproject,name = "home"),
    re_path(r'admin', admin.site.urls),
    re_path(r'register',views.register, name ="register"),
    re_path(r'login',views.loginpage, name ="loginpage"),
    re_path(r'logout',views.logoutUser, name ="logout"),
    re_path(r'result',views.result,name="result"),
    re_path(r'popular', views.popular, name ="popular"),
    re_path(r'success',views.success, name ="success"),
    re_path(r'create',views.create, name ="create"),
    path('detail/<str:project>/',views.detail,name="detail"),

]

