from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password')


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'