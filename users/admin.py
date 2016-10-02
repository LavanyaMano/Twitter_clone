from django.contrib import admin
from .models import Profile, Relationship
from tweets.models import Tweet


class TweetInline(admin.TabularInline):
    model = Tweet
    extra =1

# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#     extra =1

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio','location','birthday','profile_pic','tweet_headings','get_following','get_followers',]
    inlines =[TweetInline,]

    def tweet_headings(self,obj):
        heading = [tweet.heading for tweet in obj.tweet_set.all()]
        return ", ".join(heading)

admin.site.register(Profile,ProfileAdmin)

