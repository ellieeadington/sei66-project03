from django.forms import ModelForm, EmailField
from .models import BrewingMethod, CoffeeBean, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BrewingMethodForm(ModelForm):
    class Meta:
        model = BrewingMethod
        fields = ['method_name', 'method_bio', 'method_image']
        
        
class CoffeeBeanForm(ModelForm):
    class Meta:
        model = CoffeeBean
        fields = ['name', 'variety', 'description', 'roastery', 'date_harvested', 'image', 'location']        

class UserRegisterForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['is_cafe_owner']