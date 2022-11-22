from xml.dom import UserDataHandler
from django import forms
from django.forms import ModelForm, EmailField
from .models import BrewingMethod, CoffeeBean, Profile, Event, Review, Cafe
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class BrewingMethodForm(ModelForm):
    class Meta:
        model = BrewingMethod
        fields = ['method_name', 'method_bio']

        
class CoffeeBeanForm(ModelForm):
    class Meta:
        model = CoffeeBean
        fields = ['name', 'variety', 'description', 'roastery', 'date_harvested', 'image', 'location']        


class IsCafeOwnerForm(ModelForm):  
    is_cafe_owner = forms.BooleanField(required=False,label="Please check if you are signing up as a cafe owner today", widget=forms.CheckboxInput())
    class Meta:
        model = Profile
        fields = ['is_cafe_owner']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Choose a username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class CafeForm(ModelForm):
    
    cafe_name = forms.CharField(required=False)
    cafe_bio = forms.CharField(required=False)
    date_founded = forms.DateField(required=False)
    address_line_1 = forms.CharField(required=False)
    address_line_2 = forms.CharField(required=False)
    address_city = forms.CharField(required=False)
    address_county = forms.CharField(required=False)
    address_country = forms.CharField(required=False)
    address_postcode = forms.CharField(required=False)
    cafe_image = forms.ImageField(required=False)
    menu_image = forms.ImageField(required=False)
    cafe_website = forms.CharField(required=False)

    class Meta:
        model = Cafe
        fields = ['cafe_name', 'cafe_bio', 'date_founded', 'address_line_1', 'address_line_2', 'address_city', 'address_county', 'address_country', 'address_postcode', 'cafe_image', 'menu_image', 'cafe_website']

    def __init__(self, *args, **kwargs):
        super(CafeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'cafe-form' 


class UserUpdateForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password(self):
        return super().clean_password2()


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_type', 'event_date', 'event_time_from', 'event_time_to']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_body', 'stars']
        
        
        
