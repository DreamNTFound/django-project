from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = (
    re_path(r'^$', views.home, name="home"),
    re_path(r'^login$', views.Sign_In, name="login")
)
