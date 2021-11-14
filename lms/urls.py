from django.contrib import admin
from django.urls import path,include
from lms import views


urlpatterns = [
    
    path('',views.index,name="index"),
]