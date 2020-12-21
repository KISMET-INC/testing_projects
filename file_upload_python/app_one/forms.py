from django import forms 
from .models import *
  
class OwnerForm(forms.ModelForm): 
  
    class Meta: 
        model = Owner 
        fields = ['name']

class ImgForm(forms.ModelForm): 

       
  
    class Meta:
        model = Image
        fields = ['owner', 'pet_img']
