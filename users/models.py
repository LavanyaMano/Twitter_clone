from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank = True)
    location = models. TextField(blank= True)
    birthday = models.DateField(blank=True)
    # profile_pic= models.FileField(upload_to="images")





