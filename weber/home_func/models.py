from mongoengine import *
from weber.settings import DBNAME
connect(DBNAME)
from mongoengine.django.auth import User

class Userpost(Document):
    title = StringField(max_length=120,required=True)
    #image_path =
    publish_date = DateTimeField()
    username = StringField(max_length=120,required=True)
    permission_type=StringField(max_length=120,required=True)
    #auto_id = IntField(required=True)
    #user_id = StringField(max_length=200)

class friends(Document):
    friend1 = ReferenceField(User)
    friend2 = ListField(ReferenceField(User))
    status = ListField(IntField())

