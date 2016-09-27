from django.contrib import admin

# Register your models here.
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_display = ['heading', 'content','hashtag','posted_on',]


admin.site.register(Tweet,TweetAdmin)