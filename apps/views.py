from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DeleteView
from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.filters import ProductFilter
from apps.serializer import UserModelSerializer, UserDetailModelSerializer, UserCreateModelSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class UserCreateListApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_fields = ('first_name', 'last_name')
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateModelSerializer
        elif self.request == 'GET':
            return UserModelSerializer
        return super().get_serializer_class()


class UserDetailApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailModelSerializer


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer



