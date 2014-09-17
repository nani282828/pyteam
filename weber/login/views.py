from django.shortcuts import render
from django.shortcuts import render_to_response
#from forms import UserForm
from models import User1
from django.http import HttpResponse
from mongoengine.queryset import DoesNotExist
from django.contrib import messages
from mongoengine.django.auth import User
from django.contrib.auth import authenticate
#from django.contrib.auth.models import check_password
from mongoengine import *



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User_save = User(username=username, password=password)
        User_save.set_password(password)
        User_save.save()
        return render(request,'index.html')
    else:
        return render(request,'register.html')
def index(request):
    return render(request,"index.html",{})


def login(request):
    #User.backend = 'mongoengine.django.auth.MongoEngineBackend'
    if request.method == 'POST':
        name = request.POST['username']
        passs = request.POST['password']

        #userdata = User.objects.get(username=username)
        #user = User.objects.get(username=name)#request.POST['username'])
        user = authenticate(username=name,password=passs)#request.POST['password']):
        if user is not None:
            #user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            #print login(request, user)
            return render(request,'testing.html',{'result':'LOGIN SUCCESS'})
        else:
            return render(request,'testing.html',{'result':'FAILED'})

    else:
        return render(request,'login.html',{'result':'false'})
