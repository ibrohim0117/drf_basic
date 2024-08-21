from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from apps.serializer import UserModelSerializer, UserDetailModelSerializer


# Create your views here.


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailModelSerializer
