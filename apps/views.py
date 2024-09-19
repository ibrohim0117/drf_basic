from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.filters import ProductFilter, ProductFilterSet
from apps.models import Category, Product
from apps.serializer import UserModelSerializer, UserDetailModelSerializer, UserCreateModelSerializer, \
    CategoryModelSeCategory, ProductModelSerializer


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


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSeCategory


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filterset_fields = ('category', 'owner')
    filter_backends = DjangoFilterBackend, SearchFilter
    filterset_class = ProductFilterSet
    search_fields = ('name', 'description')



