from django.conf.urls import url

# for function based views
#from .views import tweet_detail_view, tweet_list_view

from .views import (
    TweetCreateView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView
)


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # create url for home view
    url(r'^$', TweetListView.as_view(), name= 'list'),   # /tweet/
    url(r'^create/', TweetCreateView.as_view(), name= 'create'),  # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name= 'detail'),  # /tweet/<number>/
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update') # /tweet/update/
]



