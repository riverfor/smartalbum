"""
    Album model
"""

import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    twitter_username = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    skip_flag = models.BooleanField()

class Photo(models.Model):
    user = models.ForeignKey(User)
    tweet_id = models.CharField(max_length=32)
    tweet_url = models.TextField()
    expend_url = models.TextField()
    save_date = models.DateTimeField('save date')
