#-*-coding:utf8;-*-
"""

    Get photos from twitter, and save into album

"""


import os
import traceback
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from album.models import User,Photo

from twitter import *

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)


    def handle(self, *args, **options):

        self.stdout.write('[CMD] Get from twitter start ...')

        # PROCESS
        #
        # 1 Twitter auth
        # 2 Fetch user's tweet
        #   2.1 Filter special content in tweet
        # 3 Send email if needed
        #
        
        MY_TWITTER_CREDS = os.path.expanduser(settings.TWITTER_CONF['APP_CREDS_LOCAL_PATH'])
        if not os.path.exists(MY_TWITTER_CREDS):
            oauth_dance(settings.TWITTER_CONF['APP_CREDS_LOCAL_PATH'], 
                        settings.TWITTER_CONF['CONSUMER_KEY'], 
                        settings.TWITTER_CONF['CONSUMER_SECRET'],
                        MY_TWITTER_CREDS)

        oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

        twitter = Twitter(auth=OAuth(
            oauth_token, oauth_secret, settings.TWITTER_CONF['CONSUMER_KEY'], settings.TWITTER_CONF['CONSUMER_SECRET']))

        ### Get users from db ###
        for user in User.objects.all():
            if not user.skip_flag: # still need check

                # total photo number before refresh new ones
                total_photo_number_before_check = len(Photo.objects.filter(user_id=user.id))
                

                ## check tweets
                status = twitter.statuses.user_timeline(screen_name=user.twitter_username,count=settings.LIMIT_TWEET_NUMBER_REFRESH)
                for item in status:
                    try:
                        photo = Photo.objects.get(tweet_id=item['id'])
                    except ObjectDoesNotExist:
                        if item['entities'].has_key('hashtags'):
                            for hashtag in item['entities']['hashtags']:
                                try:
                                    if str(hashtag['text']).lower() == settings.SEARCH_PIC_PATTERN:
                                        for url in item['entities']['urls']:
                                            photo = Photo()
                                            photo.tweet_id = item['id']
                                            photo.user = user
                                            photo.tweet_url = url['url']
                                            photo.expend_url  = url['expanded_url']
                                            photo.save_date = datetime.datetime.now()
                                            photo.save()
                                except:
                                    traceback.print_exc()
                print "Check %s last %s tweets" % (user.twitter_username, len(status))

                ## check if need send email 
                total_photo_number_after_check = len(Photo.objects.filter(user_id=user.id))

                checkAndSendEmail(total_photo_number_before_check, total_photo_number_after_check, 1, user)
                checkAndSendEmail(total_photo_number_before_check, total_photo_number_after_check, 2, user)
                checkAndSendEmail(total_photo_number_before_check, total_photo_number_after_check, 3, user)
                checkAndSendEmail(total_photo_number_before_check, total_photo_number_after_check, 4, user)
                checkAndSendEmail(total_photo_number_before_check, total_photo_number_after_check, 5, user)
                if total_photo_number_before_check <= 500 and total_photo_number_after_check>500:
                    user.skip_flag = True # could not check this user next
                    user.save()

            else:
                print "Skip %s"
                        
        self.stdout.write('[CMD] Get from twitter end ...')


def checkAndSendEmail(total_photo_number_before_check, total_photo_number_after_check, level, user):
    if total_photo_number_before_check <= level*100 and total_photo_number_after_check>level*100:
        pass
