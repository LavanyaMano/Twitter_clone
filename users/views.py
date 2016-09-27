from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db.models import Count
from django.contrib  import messages
from django.contrib.auth.decorators import login_required


from .models import Profile


def user_list(request):

    users = Profile.objects.all()
    context = {
    "users": users,
    }
    return render(request,"users/user_list.html",context)


def user_detail(request):
    user = get_object_or_404(Profile,pk=id)
    context = {
     "user":user,
    }

    return render(request,"users/user_detail.html",context)

