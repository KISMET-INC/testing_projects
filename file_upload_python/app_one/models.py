from django.db import models


# models.py 
class Hotel(models.Model): 
    name = models.CharField(max_length=50, blank = True, null=True) 
    

class Image(models.Model):
    hotel_Main_Img = models.ImageField(upload_to='images/') 
    hotel = models.ForeignKey(Hotel, related_name ="images", on_delete = models.CASCADE)