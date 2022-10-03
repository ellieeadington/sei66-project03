from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes_index, name='index'),

    # ROB SECTION
    
    
    
    
    
    
    
    # ASHISH SECTION
    path('acounts/signup', views.signup, name="signup")
    
    
    
    
    
    
    
    # ROB SECTION
    
    
    
    
]