from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpResponse
from models import Userpost
#from django.contrib.auth import User
from mongoengine.django.auth import User
import json
from django.views.decorators.csrf import csrf_exempt

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
        loaded_posts = Userpost.objects.filter(id__gt = post_id).limit(2)
        return render(request,'ajax_out.html',{'load_remain_posts':loaded_posts})

