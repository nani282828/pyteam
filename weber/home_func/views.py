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

def get_selected_user_info(request,username):
    f_status = 'addfriend'
    user_details = User.objects.get(username=username)
    friendslist = Friends.objects(friend1=request.user.id,myfriendslist__myfriends_ids=str(user_details.id))
    selected_udi = user_details.id
    loggeduserid = request.user.id
    if selected_udi==loggeduserid:
        f_status = 'selectedmyself'
    else:
        if friendslist:
            f_status = sel_frnd_status(user_details,selected_udi,friendslist)
    return render(request,'profile2.html',{'f_status':f_status,'user_details':user_details,'selid':selected_udi})

def sel_frnd_status(user_details,selected_udi,friendslist):
    friend_status = ''
    count = 0
    for temp in friendslist:
        for temp2 in temp.myfriendslist:
            if temp2.myfriends_ids == str(selected_udi) and temp2.status == '1' and count == 0:
                friend_status = 'alredysent'
                count = 1
            elif temp2.myfriends_ids == str(selected_udi) and temp2.status == '2' and count == 0:
                friend_status = 'friends'
                count = 1
    if count == 0:
       friend_status = 'addfriend'
    return friend_status

def add_friend(request):
    status = ''
    if request.method=='POST':
        no_friends_check = Friends.objects(friend1=request.user.id)
        if no_friends_check:
            check_requested_user = Friends.objects(friend1=request.user.id,myfriendslist__myfriends_ids=request.POST['addfriendid'])
            if check_requested_user:
                status='alredysent'
            else:
                Friends.objects(friend1=request.user.id).update_one(push__myfriendslist={'myfriends_ids':request.POST['addfriendid'],'status':'1'})
                status = "hasbeensent"
        else:
            Friends.objects.create(friend1=request.user.id,myfriendslist=[{'myfriends_ids':request.POST['addfriendid'],'status':'1'}])
            status = 'hasbeensent'
        userinfo = getuserdetailsbyid(request.POST['addfriendid'])
    return render(request,'profile2.html',{'f_status':status,'user_details':userinfo,'selid':request.POST['addfriendid']})


def reject_friend(request):
    status = ''
    if request.method=='POST':
         check_reject_user = Friends.objects(friend1=request.user.id,myfriendslist__myfriends_ids=request.POST['rejectfriendid'])
         if check_reject_user:
             f = Friends.objects(friend1=request.user.id).update_one(pull__myfriendslist={'myfriends_ids':request.POST['rejectfriendid']})
             if f:
                 status = 'rejected'
    userinfo = getuserdetailsbyid(request.POST['rejectfriendid'])
    return render(request,'profile2.html',{'f_status':status,'user_details':userinfo,'selid':request.POST['rejectfriendid']})


def getuserdetailsbyid(selected_userid):
    details = User.objects.get(id=selected_userid)
    return details


def update_userinfo(request):
    if request.method == 'POST':
        u = User.objects(id=request.user.id).update(set__username=request.POST['username'])
        if u:
            return HttpResponse('successfully saved')
        else:
            return HttpResponse('failded to save')
    else:
        return False



