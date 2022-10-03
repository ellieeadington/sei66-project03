from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes_index, name='index'),
    
    # ROB SECTION
    
    
    
    
    
    
    
    # ASHISH SECTION
    
    
    
    
    
    
    
    # ELLIE SECTION
    path('coffee_beans/', views.coffee_beans_index,name='coffee_beans_index'),
    path('coffee_beans/<int:coffee_beans_id>', views.coffee_beans_detail, name='coffee_beans_detail'),
    
    
    
    
]