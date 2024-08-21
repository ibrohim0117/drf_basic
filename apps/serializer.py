from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')


class UserCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password')

    def validate_password(self, value):
        return make_password(value)


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'