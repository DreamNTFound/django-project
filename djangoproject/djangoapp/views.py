from django.shortcuts import render
from .models import LoginForms

# Create your views here.

def home(req):
    return render(req, "base.html")

def Sign_In(req):
        return render (req, "form/login.html")
