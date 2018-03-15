from django.shortcuts import render

from .models import Tweet

# Create your views here.

# Create 
# Retrive
# Update
# Delete
# List/Search

def tweet_detail_view(request, id = 1):
    obj = Tweet.objects.get(id= id)
    print(obj.user)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", {})


def tweet_list_view(request):
    # returns a list
    queryset = Tweet.objects.all()
    for obj in queryset:
        print(obj.tweet_content)
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", {})









