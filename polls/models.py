from django.db import models
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.core.management import call_command
import sys


#class Person(models.Model):
#    userId = models.CharField(db_column='userId', primary_key=True, max_length=20)  # Field name made lowercase.
#   userPassword = models.CharField(db_column='userPassword', max_length=20)  # Field name made lowercase.
#  userName = models.CharField(db_column='userName', max_length=20)  # Field name made lowercase.

        
class Poll(models.Model):
    pollId = models.AutoField(auto_created=True, db_column='pollId', primary_key=True)  # Field name made lowercase.
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='poll',db_column='userId')  # Field name made lowercase.
    questionText = models.CharField(db_column='questionText', max_length=200, blank=False)  # Field name made lowercase.
    pollImage = models.ImageField(db_column='pollImage', max_length=50, upload_to="image/%Y/%m/%d",blank=True)  # Field name made lowercase.
    expireDate = models.DateField(db_column='expireDate', blank=False, null=True)  # Field name made lowercase.
    secretPoll = models.BooleanField(default=True, db_column='secretPoll', blank=False, null=True)  # Field name made lowercase.


class Choice(models.Model):
    choiceId = models.AutoField(auto_created=True, db_column='choiceId', primary_key=True)  # Field name made lowercase.
    pollId = models.ForeignKey(Poll, on_delete=models.CASCADE,  related_name='choice',db_column='pollId')  # Field name made lowercase.
    choiceText = models.CharField(db_column='choiceText', max_length=100)  # Field name made lowercase.
    count = models.IntegerField(default=0,blank=True)

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['poll', 'voter'], name='unique_voter_for_questions')
    ]


