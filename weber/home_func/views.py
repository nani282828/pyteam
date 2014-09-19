#from django.shortcuts import render
from forms import PostStatusForm
import json
from django.shortcuts import render
from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponse
from models import UserPost
#from mongoengine.django.auth import User
import datetime

# Create your views here.
def post_status(request):
    if request.method == 'POST':
        title = request.POST['post_text']
        post = UserPost(post_title=title)
        post.user_name = 'slkdflsjdfl'
        #post.permission_type = request.POST['permission_type']
        #post.user_name = request.user.username
        #publish_date1 = datetime.datetime.now()
        #post.publish_date1 = publish_date1
        post.save(force_insert=True,validate=False, clean=False)
        return HttpResponse(json.dumps({'post_title': request.POST['post_text']}))
    else:
        return render(request,'homepage.html',{'userpost':'no post posted'})