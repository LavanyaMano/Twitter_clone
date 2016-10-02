from django.contrib import admin

# Register your models here.
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    def username(self,instance):
        if hasattr(instance.profile, 'user'):
            return instance.profile.user.username

    list_display = ['heading', 'content','hashtag','posted_on','username',]


admin.site.register(Tweet,TweetAdmin)