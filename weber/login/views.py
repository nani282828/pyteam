from django.shortcuts import render
from django.shortcuts import render_to_response
#from forms import UserForm
from models import User1
from django.http import HttpResponse,HttpResponseRedirect
from mongoengine.queryset import DoesNotExist
from django.contrib import messages,auth
from mongoengine.django.auth import User
from django.contrib.auth import authenticate,logout
#from django.contrib.auth.models import check_password
#from mongoengine import *
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User_save = User.create_user(username=username,email=None,password=password)
        User_save.save()
        return HttpResponseRedirect('/theweber.in/')
    else:
        return render(request,'register.html')

@login_required(login_url='/theweber.in/login')
def home(request):
    if request.user.is_authenticated:
        posts = db.userpost.find()
        return render(request,'homepage.html',{'userposts': posts, 'username':request.user.username})
    else:
        return HttpResponseRedirect('/theweber.in/login')

def index(request):
    return render(request,"index.html",{})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)#request.POST['password']):
        if user is not None and user.is_active:
            #user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            auth.login(request, user)
            return HttpResponseRedirect('/theweber.in/home')
        else:
            return render(request,'login.html',{'result':'username and password not valid'})
    else:
        return render(request,'login.html',{'result':''})


"""def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/theweber.in/')"""



