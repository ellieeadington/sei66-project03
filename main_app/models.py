from django.db import models
from django.urls import reverse
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


BREWINGMETHOD = (
    ('DB', 'Drip Brewed'),
    ('P', 'Percolator'),
    ('FP', 'French Press'),
    ('C', 'Chezve'),
    ('P', 'Pour-over'),
    ('S', 'Syphon'),
    ('CM', 'Coffee Maker'),
    ('V', 'V60'),
    ('AP', 'Aeropress')
)


class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
     is_cafe_owner = models.BooleanField(default=False)
     
     def __str__(self):
        return f"is {self.user.username} a cafe owner? {self.user.profile.is_cafe_owner}"

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created: 
#         Profile.objects.create(user=instance)


TYPE = (
    ('KID', 'Children'),
    ('MUM', 'Parent and Children'),
    ('HEA', 'Health and Wellbeing'),
    ('FIT', 'Fitness'),
    ('FOO', 'Cooking and Food'),
    ('ENT', 'Entertainment'),
    ('ART', 'Arts and Crafts')
)


class CoffeeBean(models.Model):
    name = models.CharField(max_length=250)
    variety =  models.CharField(max_length=1000, choices=VARIETIES, default=VARIETIES[0][0])
    description = models.CharField(max_length=2000)
    roastery = models.CharField(max_length=250)
    date_harvested = models.CharField(max_length=250)
    image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    location = models.CharField(max_length=250)
    
    def get_absolute_url(self):
        return reverse('coffee_bean_edit', kwargs = {'cafe_id': self.id})
    def __str__(self):
        return self.variety
    def __str__(self):
        return self.roastery
    

    
# Create your models here.

class Cafe(models.Model):
    cafe_name = models.CharField(max_length=250, blank=True)
    cafe_bio = models.CharField(max_length=2500, blank=True)
    date_founded = models.DateField()
    address_line_1 = models.CharField(max_length=250, blank=True)
    address_line_2 = models.CharField(max_length=250, blank=True)
    address_city = models.CharField(max_length=250, blank=True)
    address_county = models.CharField(max_length=250, blank=True)
    address_country = models.CharField(max_length=250, blank=True)
    address_postcode = models.CharField(max_length=10, blank=True)
    cafe_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    menu_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    cafe_website = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    coffee_beans = models.ManyToManyField(CoffeeBean, blank=True)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'cafe_id': self.id})
    
    def __str__(self):
        return f"{self.cafe_name} on {self.address_city}" # NEED TO WORK OUT HOW TO RETURN TWO OBJECT FIELD NAMES - STRING OVERRIDE!!!!!
    # def __str__(self):
    #     return self.address_city
    
class Event(models.Model):

    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)   
    event_name = models.CharField(max_length=250)
    event_description = models.CharField(max_length=1000)
    event_type = models.CharField(max_length=4, choices=TYPE, default=TYPE[0][0])
    event_date = models.DateField()
    event_time_from = models.TimeField()
    event_time_to = models.TimeField()
    event_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")

    def get_absolute_url(self):
        return reverse('event_edit', kwargs = {'cafe_id': self.id})
    def __str__(self):
        return f"{self.get_event_type_display} on {self.event_date}"

        
    
class Review(models.Model):
    datetime = models.DateField(auto_now_add=True, null=True)
    stars = models.CharField(max_length=2, choices=STARS, default=STARS[0][0])
    review_title = models.CharField(max_length=250)
    review_body = models.CharField(max_length=1000)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
class CafeOpening(models.Model):
    weekday_open = models.CharField(max_length=250)
    open_from = models.TimeField()
    open_from = models.TimeField()
    
class BrewingMethod(models.Model):
    method_name = models.CharField(max_length=2, choices=BREWINGMETHOD, default=BREWINGMETHOD[0][0])
    method_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    method_bio = models.CharField(max_length=300)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('brewing_method_edit', kwargs = {'cafe_id': self.id})

    def __str__(self):
        return f"{self.get_method_name_display} on {self.method_bio}"
