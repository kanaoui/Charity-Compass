from django import forms
from . import models

class CreateCampagne(forms.ModelForm):
    class Meta:
        model = models.Campagne
        fields = ['charity_number','slug', 'nom',  'histoire', 'thumbnail',]