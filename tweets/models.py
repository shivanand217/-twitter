# import settings for auth

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
# bring all the models into the admin 
# so that admin will see it
# every time when make changes to the models do manage.py makemigrations

# class name has to be imported as models in our views

class Twee_t(models.Model):

    # a user to which this tweet is associated
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    tweet_content = models.CharField(max_length=150, default="write tweet here")
    updated = models.DateTimeField(auto_now= True)
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.tweet_content)    










