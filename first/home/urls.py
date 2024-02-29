from django.contrib import admin
from django.urls import path
from home import views
# from .views import fetch

urlpatterns = [
    # path('', views.homes, name='home'),
    # path('', views.loginpage, name='loginpage'),
    path('', views.landingpage, name='landingpage'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('pd', views.pd, name='pd'),
    path('oa', views.oa, name='oa'),
    path('plc', views.plc, name='plc'),
    path('exco', views.exco, name='exco'),
    path('cocu', views.cocu, name='cocu'),
    path('ad', views.ad, name='ad'),
    path('homes', views.homes, name='homes'),
    path('logout', views.logoutpage, name='logout'),
    # path('fetchdata', views.fetch, name='fetchdata'),
    # path('homes/', fetch, name='fetch'),
    # path('', views.landingpage, name='landingpage'),
    path('att', views.att, name='att'),
    
]

