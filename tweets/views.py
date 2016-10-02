from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm
from django.contrib import messages
from users.models import Profile


def tweet_list(request):
    tweets = Tweet.objects.all()
    context = {
    "tweets": tweets,
    "user" : request.user
    }
    return render(request,"tweets/tweet_list.html",context)

def tweet_detail(request, id):
    tweet = get_object_or_404(Tweet, pk=id)
    profile = tweet.profile
    current_profile = request.user.profile
    follows = profile.get_following()
    follows = follows.exclude(user = profile.user)
    follower = profile.get_followers()
    follower = follower.exclude(user= profile.user)
    context = {
        "tweet": tweet,
        "current_profile":current_profile,
        "profile":profile,
        "follower":follower,
        "follows":follows,
    }
    return render(request, "tweets/tweet_detail.html", context)


def tweet_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.profile = request.user.profile
            tweet.save()
            messages.success(request,"tweet created!")
            return redirect("users:user_detail", id = request.user.pk)
    else:
        form =TweetForm()

    context = {
        "form": form,
        }
    return render(request,"tweets/tweet_edit.html", context)



def tweet_edit(request,id):
    tweet = get_object_or_404(Tweet, pk=id)
    current_profile = request.user.profile
    follows = current_profile.get_following()
    follows = follows.exclude(user = current_profile.user)
    follower = current_profile.get_followers()
    follower = follower.exclude(user= current_profile.user)
    followed_profiles = [ following.followed_by for following in current_profile.following.all()]

    if request.method == "POST":
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            tweet = form.save()
            messages.success(request, "{} has been updated!".format(tweet.heading))
            return redirect("users:user_detail", id=current_profile.pk)
    else:
        form = TweetForm(instance=tweet)

    context = {
        "form": form,
        "tweet": tweet,
        "current_profile":current_profile,
        "follower":follower,
        "follows":follows,
        "followed_profiles":followed_profiles,
    }
    return render(request, "tweets/tweet_edit.html",context)


           