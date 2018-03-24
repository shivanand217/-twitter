from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from .validators import validate_tweet_content
from .validators import validate_hashtag

# Create your models here.
# bring all the models into the admin 
# so that admin will see it
# every time when make changes to the models do manage.py makemigrations


# class name has to be imported as models in our views
class Twee_t(models.Model):

    # a user to which this tweet is associated
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default= 1)
    tweet_content = models.CharField(max_length= 150, default= "write tweet here", validators= [validate_tweet_content])
    updated = models.DateTimeField(auto_now= True)
    timestamp = models.DateTimeField(auto_now_add= True)
    hashtag = models.CharField(max_length= 160, default= "put hashtag without #", validators= [validate_hashtag])

    def __str__(self):
        return str(self.tweet_content)    

    '''
    # Validation in the model
    def clean(self, *args, **kwargs):

        validation_error = []

        Tweet_content = self.tweet_content
        if Tweet_content == "abc":
            raise ValidationError("Tweet_content cannot be abc.")

        # validate hashtags
        tag = self.hashtag
        if tag in abusive_words:
            raise ValidationError("This hashtag is abusive. You can't use this.")

        # args in super(ModelName, self).clean(*args, **kwargs)

        return super(Twee_t, self).clean(*args, **kwargs)

    '''









