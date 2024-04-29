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
    path('loginpageM', views.loginpageM, name='loginpageM'),
    path('signuppageM', views.signuppageM, name='signuppageM'),
    path('pd', views.pd, name='pd'),
    path('oa', views.oa, name='oa'),
    path('plc', views.plc, name='plc'),
    path('hs', views.hs, name='hs'),
    path('exco', views.exco, name='exco'),
    path('cocu', views.cocu, name='cocu'),
    path('ad', views.ad, name='ad'),
    path('homes', views.homes, name='homes'),
    path('logout', views.logoutpage, name='logout'),
    # path('fetchdata', views.fetch, name='fetchdata'),
    # path('homes/', fetch, name='fetch'),
    # path('', views.landingpage, name='landingpage'),
    path('att', views.att, name='att'),
    path('pdm', views.pdm, name='pdm'),
    path('report', views.report, name='report'),
    path('printr', views.printr, name='printr'),
    path('homesM', views.homesM, name='homesM'),
    # path('studentData', views.studentData, name='studentData'),
    # path('display_student_data', views.display_student_data, name='display_student_data'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('get_data/', views.get_data, name='get_data'),
    path('save_table_data/', views.save_table_data, name='save_table_data'),
    path('studentData/<str:roll_number>/', views.studentData, name='student_data'),
    # path('nameM', views.nameM, name='nameM'),
    
    
]

