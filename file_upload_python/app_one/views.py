from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        ownerForm= OwnerForm(request.POST, request.FILES) 
        imageForm= ImgForm(request.POST, request.FILES) 
       
  
        if ownerForm.is_valid() and imageForm.is_valid(): 
            if request.POST['name'] != "":
                print(request.POST['name'])
                ownerForm.save()
                newOwner = Owner.objects.order_by('-id')[0]
                newImage = Image.objects.create(pet_img = request.FILES['pet_img'], owner = newOwner)
                newImage.save()
            else:
                imageForm.save()

            return redirect('success') 
    else: 
        ownerForm = OwnerForm() 
        imageForm = ImgForm() 
    return render(request, 'owner_and_pets.html', {'ownerForm' : ownerForm, 'imageForm' : imageForm }) 
  
  
def success(request): 
    
    context = {
        'owners' : Owner.objects.all()
    }
    return render(request, 'success.html', context) 

class FiraCreateView(CreateView):
    model = Image
    form_class = ImgForm
    template_name = 'owner_and_pets.html'
    success_url = '/'
