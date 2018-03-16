
from django.conf.urls import url
#from .views import tweet_detail_view, tweet_list_view

from .views import TweetDetailView, TweetListView


urlpatterns = [
    
    #url(r'^admin/', admin.site.urls),
    # create url for home view
    url(r'^$', TweetDetailView.as_view(), name= 'details'),
    url(r'^1/$', TweetListView.as_view(), name= 'list'),
]



