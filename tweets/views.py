from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm,RetweetForm
from django.contrib import messages
from users.models import Profile

def base_context(request,id):
    tweets = Tweet.objects.all()
    tweet = get_object_or_404(Tweet, pk=id)
    profile = tweet.profile
    current_profile = request.user.profile
    follows = profile.get_following()
    follows = follows.exclude(user = profile.user)
    follower = profile.get_followers()
    follower = follower.exclude(user= profile.user)
    context = {
        "tweets": tweets,
        "profile_tweet": tweet,
        "current_profile":current_profile,
        "profile":profile,
        "follower":follower,
        "follows":follows,
        "user" : request.user
    }
    return context


def tweet_list(request,id):
    context = base_context(request,id)
    return render(request,"tweets/tweet_list.html",context)

def tweet_detail(request, id):
    
    context = base_context(request,id)
    return render(request, "tweets/tweet_detail.html", context)


def tweet_new(request):

    context = base_context(request,id=1)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.profile = request.user.profile
            tweet.save()
            messages.success(request,"tweet created!")
            return redirect("users:user_detail", id=current_profile.pk)
    else:
        form =TweetForm()

    context["form"] =form 

    return render(request,"tweets/tweet_edit.html", context)



def tweet_edit(request,id):
    current_profile = request.user.profile
    tweet = get_object_or_404(Tweet, pk=id)
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
        }
    return render(request, "tweets/tweet_edit.html",context)

def retweet(request,id):
    tweet = get_object_or_404(Tweet, pk=id)
    if request.method == "POST":
        form = RetweetForm(request.POST, instance=tweet)
        if form.is_valid():
            tweet = form.save()
            messages.success(request,"Done!")
            return redirect("users:user_detail", id=current_profile.pk)
    else:
        form = TweetForm(instance=tweet)

    context = {
        "form": form,
        "tweet": tweet,
        }
    return render(request, "tweets/tweet_edit.html",context)

def tweet_delete(request,id):
    current_profile = request.user.profile
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, pk=id)
        tweet.delete()
        messages.success(request, "Tweet deleted!")
        return redirect("users:user_detail", id=current_profile.pk)
    else:
        messages.success(request, "Tweet not found!")
        return redirect("users:user_detail", id=current_profile.pk)


