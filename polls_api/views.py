from django.shortcuts import render, get_object_or_404
#from rest_framework.decorators import api_view
from polls.models import Poll,Choice,Vote
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics,permissions

# Create your views here.

class PollList(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VoteList(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self, *args, **kwargs):
        return Vote.objects.filter(voter=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(voter=self.request.user)

