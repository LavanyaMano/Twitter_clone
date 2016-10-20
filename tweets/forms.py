from django import forms
from .models import Tweet
from core.forms import BootstrapFormMixin


class  TweetForm(BootstrapFormMixin,forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('heading','content','hashtag',)

class  RetweetForm(BootstrapFormMixin,forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('retweet',)

