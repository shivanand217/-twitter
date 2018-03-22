from django.shortcuts import render

# Django builtin class based View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist 

from .models import Twee_t


''' Class based views'''
class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Twee_t.objects.all()

    '''
    def get_object(self):
        try:
            print(self.kwargs)
            pk = self.kwargs.get("pk")
            print(pk)
            li = Twee_t.objects.get(id = pk)
            return li
        except ObjectDoesNotExist:
            li = None
    '''

    def get_context_data(self, *args, **kwargs):
        context = super(TweetDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Twee_t.objects.all()

    '''    
    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        #return Twee_t.objects.get(pk= 1)
        return queryset
    '''
    
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # we can add context here
        context["another_context"] = Twee_t.objects.all()
        print(context)
        return context

'''
function based views

def tweet_detail_view(request, id= 1):
    #content = Tweet.objects.get(tweet_content= 'hello this is shiv')
    #obj     = Tweet.objects.get(id = 1)
    obj = Twee_t.objects.get(id= id)
    queried_id = 1

    greetings = "hey hello"
    msg = "queried message with id "

    context = {
        "object_detail": obj,
        "success_msg": msg,
        "greetings": greetings,
        "id": queried_id
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    # returns a list
    queryset = Twee_t.objects.all()
    for obj in queryset:
        print(obj.tweet_content)
    context = {
        "object_list": queryset
    }
    
    return render(request, "tweets/list_view.html", context)
'''