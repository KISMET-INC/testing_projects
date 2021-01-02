from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.template import Context, loader
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import StaticHTMLRenderer
from django.template.response import TemplateResponse

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

