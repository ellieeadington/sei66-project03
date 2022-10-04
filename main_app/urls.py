from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes_index, name='index'),

    # ROB SECTION
    path('cafes/<int:cafe_id>', views.cafes_detail, name='detail'),
    path('cafes/create/', views.CafeCreate.as_view(), name='cafes_create'),
    # Delete and Update for Cafes
    path('cafes/<int:pk>/update/', views.CafeUpdate.as_view(), name='cafes_update'),
    path('cafes/<int:pk>/delete/', views.CafeDelete.as_view(), name='cafes_delete'),
    
    
    
    
    
    
    
    # ASHISH SECTION
    path('accounts/signup', views.signup, name="signup"),
    
    
    
    
    
    
    

    # ELLIE SECTION
    path('coffee_beans/', views.coffee_beans_index, name='coffee_beans_index'),
    path('coffee_beans/<int:coffee_beans_id>', views.coffee_beans_detail, name='coffee_beans_detail'),
    path('profile/cafe/<int:cafe_id>',views.cafe_owner_profile, name='cafe_owner_profile'),
    path('profile/cafe/<int:cafe_id>/coffee_beans/', views.coffee_bean_create, name='coffee_bean_create'),
    


    
    
    
]