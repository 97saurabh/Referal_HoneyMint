from django.shortcuts import render
from myapp import models
from django.contrib.auth.models import User
def home(request):


    return render(request,'index.html',{})

def about(request):

    return render(request,'aboutus.html',{})
