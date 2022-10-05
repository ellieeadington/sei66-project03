import django_filters
import django_filters as filters
from django import forms


from .models import CoffeeBean

class CoffeeBeanFilter(django_filters.FilterSet):
    roastery = filters.ModelChoiceFilter(field_name = 'roastery', label='roastery', queryset = CoffeeBean.objects.all().distinct('roastery'))
    
    class Meta:
        model = CoffeeBean
        fields = ['variety', 'roastery']
