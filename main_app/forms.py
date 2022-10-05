from django.forms import ModelForm
from .models import BrewingMethod, Event

class BrewingMethodForm(ModelForm):
    class Meta:
        model = BrewingMethod
        fields = ['method_name', 'method_bio', 'method_image']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_type', 'event_date', 'event_time_from', 'event_time_to', 'event_image']