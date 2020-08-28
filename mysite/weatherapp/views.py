from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from rest_framework import permissions
from weatherapp.serializers import UserListSerializer
from weatherapp.models import User_list

# Create your views here.

class UserListViewSet(viewsets.ModelViewSet):
    queryset = User_list.objects.all()
    serializer_class = UserListSerializer