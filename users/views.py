from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db.models import Count
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile,RELATIONSHIP_STATUSES,Relationship
from .forms import UserForm
from tweets.forms import TweetForm
from tweets.models import Tweet

def base_context(request):
    
    profiles = Profile.objects.exclude(user = request.user)
    current_profile = request.user.profile
    tweets= Tweet.objects.all()
    follows = current_profile.get_following()
    follows = follows.exclude(user = current_profile.user)
    follower = current_profile.get_followers()
    follower = follower.exclude(user= current_profile.user)
    followed_profiles = [following.followed_by for following in current_profile.following.all()]

    context = {
    "profiles": profiles,
    "tweets":tweets,
    "current_profile":current_profile,
    "follower":follower,
    "follows":follows,
    "followed_profiles":followed_profiles,
    }
    return context

@login_required
def user_list(request):
    context = base_context(request)
    return render(request,"users/user_list.html",context)


def user_detail(request,id):
    context = base_context(request)
    query_set = Profile.objects
    query_set = query_set.select_related('user')
    user_profile = get_object_or_404(query_set,pk=id)
    context["user_profile"] = user_profile
    context["user_tweets"] = user_profile.tweet_set.all()
    return render(request,"users/user_detail.html",context)

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            messages.success(request,"Welcome!")
            return redirect("users:user_detail", id = user.pk)
    else:
        form =UserForm()

    context = {
    "form": form
    }
    return render(request,"users/user_edit.html", context)

def user_edit(request,id):
    # user = get_object_or_404(Profile, pk=id)
    try:
        # import pdb; pdb.set_trace()
        user= User.objects.get(pk=id).profile
        
    except:
        return redirect("users:user_new")

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, "{} profile has been updated!".format(user.user.username))
            return redirect("users:user_detail", id=user.pk)
    else:
        form = UserForm(instance=user)

    context = {
        "form": form,
        "user": user,
    }
    return render(request, "users/user_edit.html", context)

def follow(request,id):
    if request.method == "POST":
        member= Profile.objects.get(pk=id)
        request.user.profile.add_relationship(member,1)
        request.user.save()
        member.save()
        messages.success(request,"Success")
        profiles = Profile.objects.all()
        current_profile = request.user.profile
        tweets= Tweet.objects.all()
        followed_profiles = [ following.followed_by for following in current_profile.following.all()]
        context = {
        "profiles": profiles,
        "tweets":tweets,
        "current_profile":current_profile,
        "followed_profiles": followed_profiles,

        }
        return render(request,"users/user_list.html",context)

def unfollow(request,id):
    if request.method == "POST":
        member= Profile.objects.get(pk=id)
        request.user.profile.remove_relationship(member,1)
        request.user.save()
        member.save()
        messages.success(request,"Successfully removed")
        profiles = Profile.objects.all()
        current_profile = request.user.profile
        tweets= Tweet.objects.all()

        followed_profiles = [ following.followed_by for following in current_profile.following.all()]
        context = {
        "profiles": profiles,
        "tweets":tweets,
        "current_profile":current_profile,
        "followed_profiles": followed_profiles,

        }
        return render(request,"users/user_list.html",context)

def tweet_new(request):
    context = base_context(request)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            current_profile = request.user.profile
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

def tweet_delete(request,id):
    current_profile = request.user.profile
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, pk=id)
        tweet.delete()
        messages.success(request, "Tweet deleted!")
        return redirect("users:user_detail", id=current_profile.pk)
    else:
        tweet = get_object_or_404(Tweet, pk=id)
        tweet.delete()
        messages.success(request, "Tweet deleted!")
        return redirect("users:user_detail", id=current_profile.pk)


