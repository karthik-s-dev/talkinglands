from mongoengine import Document, StringField, PointField

class Point(Document):
    name = StringField(required=True)
    description = StringField()
    location = PointField(required=True)  # use to store location