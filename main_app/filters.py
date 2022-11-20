import django_filters as filters
from .models import CoffeeBean, Cafe

class CoffeeBeanFilter(filters.FilterSet):
    roastery = filters.ModelChoiceFilter(field_name = 'roastery', label='Roastery', queryset = CoffeeBean.objects.all().distinct('roastery')) 
    class Meta:
        model = CoffeeBean
        fields = ['variety', 'roastery']

class CafeFilter(filters.FilterSet):

    cafe_name = filters.ModelChoiceFilter(field_name = 'cafe_name', label='Cafe', queryset = Cafe.objects.all().distinct('cafe_name'))
    address_city = filters.ModelChoiceFilter(field_name = 'address_city', label='Location', queryset = Cafe.objects.all().distinct('address_city'))
    class Meta:
        model = Cafe
        fields = ['cafe_name', 'address_city']        
        
        

