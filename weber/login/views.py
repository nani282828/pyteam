from django.shortcuts import render
from django.shortcuts import render_to_response
#from forms import UserForm
from models import User
from django.http import HttpResponse



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User_save = User(username=username, password=password)
        User_save.save()
        return render(request,'index.html')
    else:
        return render(request,'register.html')
def index(request):
    return render(request,"index.html",{})


def login(request):
    if request.method == 'POST':
            user = User.objects.get(username=request.POST['username'])
            return render(request,'testing.html',{'user':user})
    else:
        return render(request,'login.html',{})