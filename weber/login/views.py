from django.shortcuts import render
from django.shortcuts import render_to_response
#from forms import UserForm
from models import User1
from django.http import HttpResponse
from mongoengine.queryset import DoesNotExist
from django.contrib import messages
from mongoengine.django.auth import User



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User_save = User1(username=username, password=password)
        User_save.save()
        return render(request,'index.html')
    else:
        return render(request,'register.html')
def index(request):
    return render(request,"index.html",{})


def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            userdata = User1.objects.get(username=username,password=password)
            if userdata:
                
                return render(request,'login.html', {'user': 'successfully logged in'})
            else:
                return render(request,'login.html',{'user':"enter correct details first "})
        else:
            return render(request,'login.html',{'user':''})
    except DoesNotExist:
        messages = "invalid username and password"
    return render(request,'login.html',{})
