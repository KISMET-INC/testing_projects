from django.db import models


# models.py 
class Owner(models.Model): 
    name = models.CharField(max_length=50, blank = True, null=True) 
    

class Image(models.Model):
    pet_img = models.ImageField(upload_to='images/') 
    owner = models.ForeignKey(Owner, related_name ="pet_imgs", on_delete = models.CASCADE, blank = True)