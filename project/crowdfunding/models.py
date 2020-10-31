from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    u_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=50)
    u_password = models.CharField(max_length=50)
    user_email = models.CharField(unique=True, max_length=128)
    u_total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    projects_supported = models.IntegerField(blank=True, null=True)
    
     
    class Meta:
        managed = True
        db_table = 'users'

class Project(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=264)
    description = models.CharField(max_length=1200)
    p_location = models.CharField(max_length=264, blank=True, null=True)
    category = models.CharField(max_length=128)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    goal = models.DecimalField(max_digits=65535, decimal_places=65535)
    current_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project'



class Fund(models.Model):
    p = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = True
        db_table = 'fund'