from django import forms
from .models import Twee_t

# create the form class
class TweetModelForm(forms.ModelForm):
    
    class Meta:
        # give the model name here to which this form should be added
        model = Twee_t
        fields = [
            "User",
            "Tweet_content",
            "Hashtag"
        ]

        def clean_content(self, *args, **kwargs):
            content = self.cleaned_data['tweet_content']

            if tweet_content == "abc":
                raise forms.ValidationError("Cannot be shiv")
            return content