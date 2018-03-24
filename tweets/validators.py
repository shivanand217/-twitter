from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
# bring all the models into the admin 
# so that admin will see it
# every time when make changes to the models do manage.py makemigrations

# some bad hashtags to avoid when posting a tweet
abusive_words = ["cock", "dick", "asshole", "ass", "motherfucker", "boobs", "pussy", "bitch", "fuck", "cunt",
                "acrotomophilia", "hot pocket", "anal", "anilingus", "anus", "apeshit","babeland","baby batter",
                "bastard","bbw","bdsm", "beaner","beaners","blowjob","boob","boobs", "booty", "busty","butt",
                "buttcheeks", "butthole","negro","neonazi","nigga", "zoophilia"]

# another type of validations outside the class
def validate_tweet_content(value):
    content = value
    if content == "abc":
        raise ValidationError("Tweet content cannot be ABC")

    return value

def validate_hashtag(value):
    hashtag = value.split()
    abusive = []

    for tag in hashtag:
        if tag in abusive_words:
            abusive.append(tag)
    
    if len(abusive) > 0:
        raise ValidationError("You are using abusive words. Please change that. ")

    return hashtag
