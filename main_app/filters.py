import django_filters
from django import forms


from .models import CoffeeBean

class CoffeeBeanFilter(django_filters.FilterSet):
    class Meta:
        model = CoffeeBean
        fields = ['variety', 'roastery']
        
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data, queryset, request=request, prefix=prefix)
        for f in self.filters.values():
            if isinstance(f, django_filters.ChoiceFilter):
                    f.extra.update({'widget': forms.Select(attrs={'class' : 'form-control'})})    