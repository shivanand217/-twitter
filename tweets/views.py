from django.shortcuts import render

from .models import Twee_t
# Create your views here.

# Create 
# Retrive
# Update
# Delete
# List/Search

def tweet_detail_view(request, id=1):

    #content = Tweet.objects.get(tweet_content= 'hello this is shiv')
    #obj     = Tweet.objects.get(id = 1)
    us = Twee_t.objects.get(id= id)
    print(us.tweet_content)
    
    print("queried")
    #print(us)

    return render(request, "tweets/detail_view.html", {})


def tweet_list_view(request):
    # returns a list
    queryset = Twee_t.objects.all()
    for obj in queryset:
        print(obj.tweet_content)
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", {})

