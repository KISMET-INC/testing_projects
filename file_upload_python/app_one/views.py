from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        hotelForm= HotelForm(request.POST, request.FILES) 
        imageForm= ImgForm(request.POST, request.FILES) 
       
  
        if hotelForm.is_valid() and imageForm.is_valid(): 
            if request.POST['name'] != "":
                print(request.POST['name'])
                hotelForm.save()
                newHotel = Hotel.objects.order_by('-id')[0]
                newImage = Image.objects.create(hotel_Main_Img = request.FILES['hotel_Main_Img'], hotel = newHotel)
                newImage.save()
            else:
                imageForm.save()

            return redirect('success') 
    else: 
        hotelForm = HotelForm() 
        imageForm = ImgForm() 
    return render(request, 'hotel_image_form.html', {'hotelForm' : hotelForm, 'imageForm' : imageForm }) 
  
  
def success(request): 
    
    context = {
        'hotels' : Hotel.objects.all()
    }
    return render(request, 'success.html', context) 