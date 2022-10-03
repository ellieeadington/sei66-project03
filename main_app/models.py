from django.db import models

# Create your models here.
Days = (
    ('Chemex', 'Chemex')
    ('Tue', '')
    ('Wed', 'Wednesday')
    ('Thr', 'Thursday')
    ('Fri', 'Friday')
    ('Sat', 'Saturday')
    ('Sun', 'Sunday')
)

class Cafe:
    cafe_name = models.CharField(max_length=250),
    cafe_bio = models.CharField(max_length=2500),
    date_founded = models.DateField(),
    address_line_1 = models.CharField(max_length=250),
    address_line_2 = models.CharField(max_length=250),
    address_city = models.CharField(max_length=250),
    address_county = models.CharField(250),
    address_country = models.CharField(250),
    address_postcode = models.CharField(10),
    cafe_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded"),
    menu_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    
    
    