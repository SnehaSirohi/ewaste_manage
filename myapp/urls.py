from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='myapp'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("login", views.login, name='login'),
    path("loginall", views.loginall, name='loginall'),
    path("donor_form", views.donor_form, name='donor_form'),
    path("dashboard", views.dashboard, name='dashboard'),
]
