from django.shortcuts import render
from users.models import Profile
from tweets.models import Tweet


def index(request):
    profile = Profile.objects.all()
    tweets = Tweet.objects.all()

    context = {
    "profile" : profile,
    "tweets" : tweets,
    }
    return render(request,"core/index.html",context)


