from xml.dom import UserDataHandler
from django.forms import ModelForm, EmailField
from .models import BrewingMethod, CoffeeBean, Profile, Event, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BrewingMethodForm(ModelForm):
    class Meta:
        model = BrewingMethod
        fields = ['method_name', 'method_bio']

        
class CoffeeBeanForm(ModelForm):
    class Meta:
        model = CoffeeBean
        fields = ['name', 'variety', 'description', 'roastery', 'date_harvested', 'image', 'location']        

class UserRegisterForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password(self):
        return super().clean_password2()

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['is_cafe_owner']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_type', 'event_date', 'event_time_from', 'event_time_to']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_body', 'stars']
        
        
