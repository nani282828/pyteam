from mongoengine import *
from weber.settings import DBNAME
connect(DBNAME)
import datetime


# Create your models here.
class UserPost(Document):
    post_title = StringField(max_length=120,required=True)
    #image_path =
    #publish_date1 = DateTimeField(default=datetime.datetime.now)
    #permission_type = StringField()
    user_name = StringField()