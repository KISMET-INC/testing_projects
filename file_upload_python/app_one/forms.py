from django import forms 
from .models import *
from croppie.fields import CroppieField


class OwnerForm(forms.ModelForm): 
  
    class Meta: 
        model = Owner 
        fields = ['name']

class ImgForm(forms.ModelForm): 
    image = CroppieField()

    class Meta:
        model = Image
        fields ='__all__'
   