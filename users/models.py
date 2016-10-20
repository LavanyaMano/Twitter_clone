from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=200,blank = True)
    location = models. CharField(max_length=100,blank= True)
    birthday = models.DateField(blank=True)
    profile_pic= models.CharField(max_length=200,blank=True,default = "http://i164.photobucket.com/albums/u8/hemi1hemi/COLOR/COL9-6.jpg")
    relationships = models.ManyToManyField('self',through ="Relationship",symmetrical=False,related_name='related_to',)

    def __str__(self):

        return self.user.username

    def add_relationship(self, profile, status):
        relationship, created = Relationship.objects.get_or_create(
            following=self,
            followed_by=profile,
            status=status)
        return relationship

    def remove_relationship(self, profile, status):
        Relationship.objects.filter(
            following=self,
            followed_by=profile,
            status=status).delete()
        return 

    def get_relationships(self, status):
        return self.relationships.filter(
            followed_by__status=status,
            followed_by__following=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            following__status=status,
            following__followed_by=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)




class Relationship(models.Model):
    following = models.ForeignKey(Profile, related_name='following')
    followed_by = models.ForeignKey(Profile, related_name='followed_by')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)


    