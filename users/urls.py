from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$',views.user_list,name='user_list'),
 url(r'^(?P<id>\d+)/$',views.user_detail,name='user_detail'),
 url(r'^new/$',views.user_new,name='user_new'),
 url(r'^user/(?P<id>\d+)/edit$',views.user_edit,name='user_edit'),
 url(r'^user/(?P<id>\d+)/follow$',views.follow,name='follow'),
 url(r'^user/(?P<id>\d+)/unfollow$',views.unfollow,name='unfollow'),
 url(r'^user/tweet_new$',views.tweet_new,name='tweet_new'),
 url(r'^user/(?P<id>\d+)/tweet_edit$',views.tweet_edit,name='tweet_edit'),
 url(r'^user/(?P<id>\d+)/tweet_delete$',views.tweet_delete,name='tweet_delete'),
]