from django.db import models

# Create your models here.

# bring all the models into the admin 
# so that admin will see it

class Tweet(models.Model):

    this_is_a_tweet = models.TextField(default="content1")

    def __str__(self):
        return str(self.this_is_a_tweet)