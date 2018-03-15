
from django.conf.urls import url

from .views import tweet_detail_view, tweet_list_view


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # create url for home view
    url(r'^$', tweet_list_view, name= 'details'),
    url(r'^1/$', tweet_detail_view, name= 'list'),
]
