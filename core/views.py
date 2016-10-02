from django.shortcuts import render
from tweets.models import Tweet


def index(request):

    
    return render(request,"core/index.html")


def home(request):

    
    return render(request,"core/home.html")

