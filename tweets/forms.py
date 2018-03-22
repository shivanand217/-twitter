from django import forms
from .models import Twee_t

# create the form class
class TweetModelForm(forms.ModelForm):
    
    class Meta:
        # give the model name here to which this form should be added
        model = Twee_t

        fields = [
            "user",
            "tweet_content",
            #"hashtag"
        ]

        def clean_content(self, *args, **kwargs):
            content = self.cleaned_data['tweet_content']
            if tweet_content == "abc":
                raise forms.ValidationError("Cannot be ABC")
            #tag = self.cleaned_data['hashtag']
            city = self.cleaned_data['city']
            return content