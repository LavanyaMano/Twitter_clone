from django import forms
from .models import Profile
from core.forms import BootstrapFormMixin
from django.http import HttpRequest



class UserForm(BootstrapFormMixin,forms.ModelForm):

    class Meta:
        model = Profile
        exclude=['user']
        fields = ('bio','location','birthday','profile_pic',)

