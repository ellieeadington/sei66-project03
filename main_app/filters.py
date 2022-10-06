import django_filters
import django_filters as filters
from django import forms
from .models import CoffeeBean, Cafe

class CoffeeBeanFilter(django_filters.FilterSet):
    roastery = filters.ModelChoiceFilter(field_name = 'roastery', label='roastery', queryset = CoffeeBean.objects.all().distinct('roastery'))
    
    class Meta:
        model = CoffeeBean
        fields = ['variety', 'roastery']

class CafeFilter(django_filters.FilterSet):
    cafe_name = filters.ModelChoiceFilter(field_name = 'cafe_name', label='cafe_name', queryset = Cafe.objects.all().distinct('cafe_name'))
    address_city = filters.ModelChoiceFilter(field_name = 'address_city', label='address_city', queryset = Cafe.objects.all().distinct('address_city'))
    class Meta:
        model = Cafe
        fields = ['cafe_name', 'address_city']        
        
        

