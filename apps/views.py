from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.filters import ProductFilter, ProductFilterSet
from apps.models import Category, Product
from apps.serializer import UserModelSerializer, UserDetailModelSerializer, UserCreateModelSerializer, \
    CategoryModelSeCategory, ProductModelSerializer


# class UserListApiView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer


class UserListApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True).data
        # print(serializer)

        data = {
            'status': f'Foydalanuvchilar soni: {len(serializer)}',
            'users': serializer
        }
        return Response(data)


# class UserCreateApiView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateModelSerializer


class UserCreateApiView(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        serializer = UserCreateModelSerializer(data=data)
        if serializer.is_valid():
            # print(True)
            serializer.save()
            data = {
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# class UserDetailApiView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailModelSerializer


class UserDetailApiView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserDetailModelSerializer(user).data
            print(serializer)
            return Response(serializer)
        except:
            return Response("No")


# class UserUpdateApiView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer

class UserUpdateApiView(APIView):
    def put(self, request, pk):
        # user = User.objects.get(id=pk)
        user = get_object_or_404(User.objects.all(), id=pk)
        serializer = UserModelSerializer(instance=user, data=request.data, partial=True)
        print(user)
        if serializer.is_valid():
            serializer.save()
        return Response("OK")

# class UserRetrieveAPIView(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer


class UserRetrieveAPIView(APIView):

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response('OK', status=status.HTTP_200_OK)


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



