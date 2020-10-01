from django.db import models

class Site_user(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    show_only_nickname = models.BooleanField()
    created_at = models.DateTimeField('Created at')


class Swearing(models.Model):
    swearing = models.CharField(max_length=255)
    language = models.CharField(max_length=3)
    confirmed = models.BooleanField()
    user = models.ForeignKey(Site_user, models.SET_NULL,
    	blank=True,
    	null=True,)
    created_at = models.DateTimeField('Created at')

