from mongoengine import Document, StringField, PointField

class Point(Document):
    name = StringField(required=True)
    description = StringField()
    location = PointField(required=True)  # use to store location

    meta = {
        'indexes': [
            {
                'fields': ['$location'],  # The '$' prefix tells MongoEngine to use a 2dsphere index
            }
        ]
    }