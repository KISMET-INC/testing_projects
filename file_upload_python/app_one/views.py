from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form2 = HotelForm(request.POST, request.FILES) 
        form = ImgForm(request.POST, request.FILES) 
       
  
        if form2.is_valid() and form.is_valid(): 
            if request.POST['name'] != "":
                print(request.POST['name'])
                form2.save()
                newHotel = Hotel.objects.order_by('-id')[0]
                newImage = Image.objects.create(hotel_Main_Img = request.FILES['hotel_Main_Img'], hotel = newHotel)
                newImage.save()
            else:
                form.save()

            return redirect('success') 
    else: 
        form2 = HotelForm() 
        form = ImgForm() 
    return render(request, 'hotel_image_form.html', {'form2' : form2, 'form' : form, }) 
  
  
def success(request): 
    
    context = {
        'hotels' : Hotel.objects.all()
    }
    return render(request, 'success.html', context) 