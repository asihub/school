from django.forms import ModelForm, DateField
from .models import Event
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
 

class EventForm(ModelForm):
    
    ev_date = DateField(widget=SelectDateWidget(), label="На котрий день", initial=date.today())
    
    class Meta:
        model = Event
        fields = ["title", "ev_date", "ev_time", "place", "note", ]