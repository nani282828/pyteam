from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpResponse
from models import Userpost
#from django.contrib.auth import User
from mongoengine.django.auth import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

import datetime

# Create your views here.
def post_status(request):
    if request.method == 'POST':
        title = request.POST['post_text']
        post = Userpost(title=title)
        post.username = request.user.username
        post.publish_date = datetime.datetime.now()
        post.permission_type = request.POST['permission_type']
        post.save()
        return HttpResponse(json.dumps({'post_title': request.POST['post_text'],'publish_date':str(datetime.datetime.now()),'permission_type':request.POST['permission_type'],'username':request.user.username}))
    else:
        return render(request,'homepage.html',{'userpost':'no post posted'})



def load_scroll_posts(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        loaded_posts = Userpost.objects.filter(id__lt = post_id,permission_type=1).limit(20).order_by('-publish_date')
        return render(request,'ajax_out.html',{'load_remain_posts':loaded_posts,'action' : 'loadscrollposts'})


@login_required(login_url='/theweber.in/login')
def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']

    else:
        search_text = ''

    names = User.objects.filter(username__contains=search_text)

    return render(request,'ajax_out.html',{'matched_friends':names,'action' : 'searchfriendsnames'})

def frnd_requests(request):
    if request.method == 'POST':
        try:

            if friends.objects.get(friend1 = User.objects.get(email = request.user.email)):

                #u.save()
                return HttpResponse(json.dumps({'to_user':'already added session user'}))
        except:
            to_user = request.POST['to_user']
            friend1 = User.objects.get(email=request.user.email)
            friend2 = User.objects.get(email=to_user)
            friends(friend1=friend1, friend2=[friend2]).save()
            return HttpResponse(json.dumps({'to_user':'new session user added'}))

def profile_info(request):
    if request.method=='GET':
        return HttpResponseRedirect('/theweber.in/profile');