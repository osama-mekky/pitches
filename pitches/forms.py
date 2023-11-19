from .models import *
from django import forms
from django.forms import ModelForm



class RestaurantForm(forms.ModelForm):

    class Meta:
        model = OpeningHours

        fields = ('from_hour', 'to_hour','timing',)
        widgets = {
            #'made_on': DateInput(attrs={'class':'form-control'}),
            #'period':forms.Select(attrs={'class':'form-control'}),
            'from_hour':forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'),attrs={'type':'datetime-local','class':'form-control'}),
            'to_hour':forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'),attrs={'type':'datetime-local','class':'form-control'}),
            'timing':forms.Select(attrs={'class':'form-control'}),
        }