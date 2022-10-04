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
    
    path('cafes/<int:cafe_id>/add_brewing_method/', views.add_brewing_method, name='add_brewing_method'),
    
    
    
    
    
    
    # ASHISH SECTION
    path('acounts/signup', views.signup, name="signup"),
    
    
    
    
    
    
    

    # ELLIE SECTION
    path('coffee_beans/', views.coffee_beans_index, name='coffee_beans_index'),
    path('coffee_beans/<int:coffee_beans_id>', views.coffee_beans_detail, name='coffee_beans_detail'),
    path('profile/cafe/<int:cafe_id>',views.cafe_owner_profile, name='cafe_owner_profile'),
    path('profile/cafe/<int:cafe_id>/coffee_beans/', views.coffee_bean_edit, name='coffee_bean_edit'),
    path('profile/cafe/<int:cafe_id>/coffee_beans/add_coffee_bean/', views.add_coffee_bean, name='add_coffee_bean'),
    path('profile/cafe/<int:pk>/coffee_beans/update/', views.CoffeeBeanUpdate.as_view(), name='coffee_bean_update'),
    path('profile/cafe/<int:pk>/coffee_beans/delete/', views.CoffeeBeanDelete.as_view(), name='coffee_bean_delete'),
    


    
    
    
]