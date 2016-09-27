from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Tweet

def tweet_list(request):
    tweets = Tweet.objects.all()
    
    context = {
    "tweets": tweets,
    }
    return render(request,"tweets/tweet_list.html",context)


