from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from .models import *
from .serializers import *

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListByIDView(generics.ListCreateAPIView):
    def get_queryset(self):
        id_value = self.kwargs.get('id_value')
        return User.objects.filter(id=id_value)
    serializer_class = UserSerializer

class MeetingListCreateView(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class MeetingListByIDView(generics.ListCreateAPIView):
    def get_queryset(self):
        id_value = self.kwargs.get('id_value')
        return Meeting.objects.filter(id=id_value)
    serializer_class = MeetingSerializer

class MeetingListByUserView(generics.ListCreateAPIView):
    def get_queryset(self):
        user_id_value=self.kwargs.get('user_id_value')
        return Meeting.objects.filter(Q(scheduler__id=user_id_value) | Q(attendee__id=user_id_value)).order_by('start_date')
    serializer_class = MeetingSerializer

class ActionItemListCreateView(generics.ListCreateAPIView):
    queryset = ActionItem.objects.all()
    serializer_class = ActionItemSerializer

class ActionItemListByIDView(generics.ListCreateAPIView):
    def get_queryset(self):
        id_value = self.kwargs.get('id_value')
        return ActionItem.objects.filter(id=id_value)
    serializer_class = ActionItemSerializer

class ActionItemListByUserView(generics.ListCreateAPIView):
    def get_queryset(self):
        user_id_value=self.kwargs.get('user_id_value')
        return ActionItem.objects.filter(Q(assignee__id=user_id_value))
    serializer_class = ActionItemSerializer

class ActionItemListByMeetingView(generics.ListCreateAPIView):
    def get_queryset(self):
        meeting_id_value=self.kwargs.get('meeting_id_value')
        return ActionItem.objects.filter(Q(assignee__id=meeting_id_value))
    serializer_class = ActionItemSerializer
