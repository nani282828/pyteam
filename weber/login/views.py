from django.shortcuts import render
from django.shortcuts import render_to_response
#from forms import UserForm
from models import User
from django.http import HttpResponse



# Create your views here.
"""def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            User_save = User1(username=username, password=password)
            User_save.save()
            user_details = User1.objects()
            return render(request,'index.html', {'username':username, 'password': password, 'saved': 'yes',
                                                'user_details': user_details})
    else:
        return render(request,'index.html',{'username':'not set','password':'not set','saved':'no'})"""

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
    from django.contrib.auth import login
    from mongoengine.django.auth import User
    from mongoengine.queryset import DoesNotExist
    from django.contrib import messages
    try:
        if request.method == 'POST':
            user = User.objects.get(username=request.POST['username'])
            if user.check_password(request.POST['password']):
                #return render(request,'testing.html', {'password':'ok'})
                user.backend = 'mongoengine.django.auth.MongoEngineBackend'
                print login(request, user)
                #request.session.set_expiry(60 * 60 * 1) # 1 hour timeout
                print "return"
                return render(request,"index.html",{})#redirect('index')
            else:
                print "malament"
                messages.add_message(request,messages.ERROR,u"Incorrect login name or password !")
    except DoesNotExist:
        messages.add_message(request,messages.ERROR,u"Incorrect login name or password !")
    return render(request, 'login.html', {})
"""
def logout(request):#NOT TESTED
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')
def createuser(request):
    connect('reborn')
    User.create_user('boba','bobpass','bobsaget@fullhouse.gov')
    return HttpResponse("SAVED")


    """
"""sdfsdfsdfsdfdsf"""
