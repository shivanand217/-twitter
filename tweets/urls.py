
from django.conf.urls import url
#from .views import tweet_detail_view, tweet_list_view

from .views import TweetDetailView, TweetListView


urlpatterns = [
    
    #url(r'^admin/', admin.site.urls),
    # create url for home view
    url(r'^$', TweetListView.as_view(), name= 'list'), #  maps to /tweet/
    url(r'^(?P<abc>\d+)/$', TweetDetailView.as_view(), name= 'detail') # maps to /tweet/1/

]



