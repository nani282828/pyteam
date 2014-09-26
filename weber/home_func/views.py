from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpResponse
from models import Userpost
#from django.contrib.auth import User
from mongoengine.django.auth import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from models import Friends
from models import myfriends
from django import template

import datetime

# Create your views here.
def post_status(request):
    if request.method == 'POST':
        new_post = Userpost.objects.create(title=request.POST['post_text'],username=request.user.username,publish_date=datetime.datetime.now(),permission_type=request.POST['permission_type'])
        return render(request,'ajax_out.html',{'up':new_post,'action' : 'new_post_posted'})
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

def profile_info(request,username):
    user_details = User.objects.get(username=username)
    friendslist = Friends.objects(friend1=request.user.id)
    return render(request,'profile.html',{'user1':user_details,'friendslist':friendslist,'userid':str(user_details.id)})

def update_userinfo(request):
    if request.method == 'POST':
        u = User.objects(id=request.user.id).update(set__username=request.POST['username'])
        if u:
            return HttpResponse('successfully saved')
        else:
            return HttpResponse('failded to save')

    else:
        return false




def frnd_request_sent(request):
    if request.method=='POST':
        try:
            rs = Friends.objects.get(friend1=request.user.id)
            if rs:
                Friends.objects(friend1=request.user.id).update_one(push__myfriendslist={'myfriends_ids':request.POST['tofriend'],'status':'1'})
                return HttpResponse('yes your are in list')
        except Exception as e:
            add_friend = myfriends(myfriends_ids=request.POST['tofriend'],status='1')
            f = Friends(friend1=request.user.id,myfriendslist=[add_friend])
            f.save()
            return HttpResponse('SAVED')


