from mongoengine import *
from weber.settings import DBNAME
connect(DBNAME)

class Userpost(Document):
    title = StringField(max_length=120,required=True)
    #image_path =
    publish_date = DateTimeField()
    username = StringField(max_length=120,required=True)
    permission_type=StringField(max_length=120,required=True)

