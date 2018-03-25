from django import forms
from .models import Twee_t

# create the form class

class TweetModelForm(forms.ModelForm):
# give here everything you want to show in your models    
    class Meta:
        # give the model name here to which this form should be added
        model = Twee_t
        
        # give the fields 
        fields = [  
            #"user",
            "tweet_content",
            "hashtag"
        ]

        # validations below here will override the default validators
    