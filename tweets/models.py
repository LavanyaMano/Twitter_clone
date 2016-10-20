from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Tweet(models.Model):
    heading = models.CharField(max_length =50)
    content = models.CharField(max_length=140,blank = True)
    hashtag = models. CharField(max_length=20,blank= True)
    posted_on = models.DateField(auto_now_add=True)
    profile = models.ForeignKey('users.Profile',null=True)
    retweet = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.heading



