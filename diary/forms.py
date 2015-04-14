from django.forms import ModelForm, DateField
from django.forms.extras.widgets import SelectDateWidget
from diary.models import Diary
from datetime import date



class DiaryForm(ModelForm):
    
    hw_date = DateField(widget=SelectDateWidget(), label="На котрий день", initial=date.today())
   
    class Meta:
        model = Diary
        fields = ["lesson", "hw_date", "hw_descr"]