from django.contrib import admin

from .models import BrewingMethod, CoffeeBean,Cafe

# Register your models here.

admin.site.register(CoffeeBean)
admin.site.register(Cafe)
admin.site.register(BrewingMethod)

