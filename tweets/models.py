from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
# bring all the models into the admin 
# so that admin will see it
# every time when make changes to the models do manage.py makemigrations

# class name has to be imported as models in our views
class Twee_t(models.Model):
    # a user to which this tweet is associated
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default= 1)
    tweet_content = models.CharField(max_length= 150, default= "write tweet here")
    updated = models.DateTimeField(auto_now= True)
    timestamp = models.DateTimeField(auto_now_add= True)
    hashtag = models.CharField(max_length= 160, default= "put your hashtag here")
    College_name = models.CharField(max_length= 200, default= "Institute if engineering and management")
    City_name = models.CharField(max_length= 20, default= "Patna")
    State = models.CharField(max_length= 20, default= "Bihar")
    Phone = models.IntegerField(default= 7004602281)
    
    # bad hashtags
    abusive_words = ["cock", "dick", "asshole", "ass", "motherfucker", "boobs", "pussy", "bitch", "fuck", "cunt"
                    , "acrotomophilia","hot pocket", "anal", "anilingus", "anus","apeshit","babeland","baby batter",
                    "bastard","bbw","bdsm","beaner","beaners","blowjob","boob","boobs","booty","busty","butt",
                    "buttcheeks", "butthole","negro","neonazi","nigga","zoophilia"]

    def __str__(self):
        return str(self.tweet_content)    

    # Validation in the model
    def clean(self, *args, **kwargs):
        content = self.tweet_content
        if content == "abc":
            raise ValidationError("Cannot be abc")

        # args in super(ModelName, self).clean(*args, **kwargs)
        return super(Twee_t, self).clean(*args, **kwargs)










