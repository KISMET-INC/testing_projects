from django import forms 
from .models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name']

class ImgForm(forms.ModelForm): 

       
  
    class Meta:
        model = Image
        fields = ['hotel', 'hotel_Main_Img']
