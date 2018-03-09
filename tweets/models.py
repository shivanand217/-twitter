
# import settings for auth

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# bring all the models into the admin 
# so that admin will see it
# every time when make changes to the models do manage.py makemigrations

class Tweet(models.Model):    
    # a user to which this tweet is associated
    tweet_content = models.CharField(max_length=140,default="post your tweet here")
    
    updated = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(default=timezone.now)

    #tweet_number = models.IntegerField(default=1)









