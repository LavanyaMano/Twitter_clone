from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db.models import Count
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Profile,RELATIONSHIP_STATUSES,Relationship
from .forms import UserForm
from tweets.models import Tweet

@login_required
def user_list(request):
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
    return render(request,"users/user_list.html",context)


def user_detail(request,id):
    profile = get_object_or_404(Profile,pk=id)
    tweets = profile.tweet_set.all()
    follows = profile.get_following()
    follows = follows.exclude(user = profile.user)
    follower = profile.get_followers()
    follower = follower.exclude(user= profile.user)
    context = {
     "profile":profile,
     "tweets":tweets,
     "follower":follower,
     "follows":follows,
    }
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



