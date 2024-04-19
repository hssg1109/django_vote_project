from django.db import models
from django.conf import settings


import sys

        
class Poll(models.Model):
    pollId = models.AutoField(auto_created=True, db_column='pollId', primary_key=True)  # Field name made lowercase.
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='polls',db_column='userId',null=True)  # Field name made lowercase.
    questionText = models.CharField(db_column='questionText', max_length=200, blank=False)  # Field name made lowercase.
    pollImage = models.ImageField(db_column='pollImage', max_length=50, upload_to="image/%Y/%m/%d",blank=False)  # Field name made lowercase.
    expireDate = models.DateField(db_column='expireDate', blank=False)  # Field name made lowercase.
    secretPoll = models.BooleanField(default=True, db_column='secretPoll', blank=False)  # Field name made lowercase.
    total = models.IntegerField(default=0)

    def __str__(self):
        return f'[{self.questionText}] /작성자: {self.userId}'


class Choice(models.Model):
    choiceId = models.AutoField(auto_created=True, db_column='choiceId', primary_key=True)  # Field name made lowercase.
    pollId = models.ForeignKey(Poll, on_delete=models.CASCADE,  related_name='choice',db_column='pollId')  # Field name made lowercase.
    choiceText = models.CharField(db_column='choiceText', max_length=100,blank=True)  # Field name made lowercase.
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'[{self.pollId.questionText}] 질문내용: {self.choiceText}'

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE,related_name='vote')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE,related_name='vote')
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='vote',null=True)

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['poll', 'voter'], name='unique_voter_for_questions')
    ]


