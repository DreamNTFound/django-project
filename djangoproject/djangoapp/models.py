from django.db import models

# Create your models here.

class LoginForms(models.Model):
    username  = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    confpassw =  models.CharField(max_length=250)