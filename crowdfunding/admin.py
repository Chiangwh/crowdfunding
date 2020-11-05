from django.contrib import admin
from django.contrib.auth.models import *

from .models import Project, Fund
from django.db import models


# Register your models here.

admin.site.site_header= "Profund's Admin Dashboard"


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','description','location','category')


class FundAdmin(admin.ModelAdmin):
    list_display = ('p_id','u_id','created_at','amount')

admin.site.register(Project,ProjectAdmin)
admin.site.register(Fund,FundAdmin)





