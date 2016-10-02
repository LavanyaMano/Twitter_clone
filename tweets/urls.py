from django.conf.urls import url
from . import views

urlpatterns= [

 url(r'^$',views.tweet_list,name='tweet_list'),
 url(r'^tweets/(?P<id>\d+)/$',views.tweet_detail,name='tweet_detail'),
 url(r'^new/$',views.tweet_new,name='tweet_new'),
 url(r'^tweet/(?P<id>\d+)/edit/$',views.tweet_edit,name='tweet_edit'),
]