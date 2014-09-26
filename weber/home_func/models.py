from mongoengine import *
from weber.settings import DBNAME
connect(DBNAME)
from mongoengine.django.auth import User

class Userpost(Document):
    title = StringField(max_length=120,required=True)
    #image_path =
    publish_date = DateTimeField()
    username = StringField(max_length=120,required=True)
    permission_type=IntField()
    #auto_id = IntField(required=True)
    #user_id = StringField(max_length=200)
class myfriends(EmbeddedDocument):
    myfriends_ids = StringField()
    status = StringField()

class Friends(Document):
    friend1 = ReferenceField(User)
    myfriendslist = ListField(EmbeddedDocumentField(myfriends))






