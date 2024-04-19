from rest_framework import serializers
from polls.models import Poll,Choice,Vote
from django.contrib.auth.models import User

class ChoiceSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Choice
        fields = ['choiceText', 'votes_count']
    
    def get_votes_count(self, obj):
        return obj.vote.count()

class PollSerializer(serializers.ModelSerializer):
        #pollImage = serializers.CharField(max_length=None, allow_null=True, required=False)
        userId = serializers.ReadOnlyField(source='userId.username')
        choice = ChoiceSerializer(many=True, read_only=True)
        class Meta:
             model = Poll
             fields = ['pollId','userId','questionText','pollImage','choice','expireDate','secretPoll','total']


class UserSerializer(serializers.ModelSerializer):
        #polls = serializers.PrimaryKeyRelatedField(many=True, queryset=Poll.objects.all())
        polls = serializers.StringRelatedField(many=True, read_only=True)
        class Meta:
               model = User
               fields = ['id','username','first_name','polls']

class VoteSerializer(serializers.ModelSerializer):    
    voter = serializers.ReadOnlyField(source='voter.username')
        
    class Meta:
        model = Vote
        fields = ['id', 'poll', 'choice', 'voter']

       