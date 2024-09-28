from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Category, Product


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email')


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


# class CategoryModelSeCategory(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'slug')


class CategoryModelSeCategory(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)


class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'slug', 'image', 'category', 'description', 'owner')