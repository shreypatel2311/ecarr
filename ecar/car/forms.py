from django import forms
from .models import *

class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = '__all__'
        fields = ('name','price','cartype','carvarient','brand','Engine','fuel','exterior','comfort','capacity','year','is_featured','created_date','image1','image2','image3')