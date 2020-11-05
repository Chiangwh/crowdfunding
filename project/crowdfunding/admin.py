from django.contrib import admin
from . import models
from .models import Project, Fund

# Register your models here.
admin.site.register(Project)
admin.site.register(Fund)