from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

STARS = (
    ('5', '★★★★★'),
    ('4', '★★★★'),
    ('3', '★★★'),
    ('2', '★★'),
    ('1', '★'),    
)

VARIETIES = (
    ('A', 'Arabica'),
    ('R', 'Robusta'),
    ('L', 'Liberica'),
    ('E', 'Excelsa')
)
# Create your models here.
class Cafe(models.Model):
    cafe_name = models.CharField(max_length=250)
    cafe_bio = models.CharField(max_length=2500)
    date_founded = models.DateField()
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    address_city = models.CharField(max_length=250)
    address_county = models.CharField(max_length=250)
    address_country = models.CharField(max_length=250)
    address_postcode = models.CharField(max_length=10)
    cafe_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    menu_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    cafe_website = models.CharField(max_length=1000)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Event(models.Model):

    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)   
    event_name = models.CharField(max_length=250)
    event_description = models.CharField(max_length=1000)
    event_weekday = models.CharField(max_length=20)
    event_time_from = models.TimeField()
    event_time_to = models.TimeField()
    event_image = models.CharField(max_length=1000)
    
class Review(models.Model):
    datetime = models.DateTimeField()
    stars = models.CharField(max_length=2, choices=STARS, default=STARS[0][0])
    review_title = models.CharField(max_length=250)
    review_body = models.CharField(max_length=1000)

class CoffeeBean(models.Model):
    coffee_bean_name = models.CharField(max_length=250)
    coffee_bean_variety =  models.CharField(max_length=1000, choices=VARIETIES, default=VARIETIES[0][0])
    coffee_bean_description = models.CharField(max_length=2000)
    roastery_name = models.CharField(max_length=250)
    date_harvested = models.CharField(max_length=250)
    coffee_bean_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    coffee_bean_location = models.CharField(max_length=250)
    
class CafeOpening(models.Model):
    weekday_open = models.CharField(max_length=250)
    open_from = models.TimeField()
    open_from = models.TimeField()
    
class BrewingMethod(models.Model):
    brewing_method = models.CharField(max_length=250)
    
    
        
    
    
    
        

    
    
    
    