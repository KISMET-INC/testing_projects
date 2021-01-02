from django.shortcuts import render, HttpResponse, redirect
from .models import *


def returnData(request):
    user = User.objects.get(name='kris')
    user.age = user.age+1;
    user.save()
    context = {
        'user': user
    }
    print(user.age)
    return render(request, 'snip.html',context)



def index(request):
    user = User.objects.get(name='kris')
    context = {
        'user': user
    }

    return render(request, 'index.html', context)

