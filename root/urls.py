"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.views import (UserListApiView, UserCreateApiView,
                        UserDetailApiView, UserUpdateApiView,
                        UserRetrieveAPIView, UserCreateListApiView, ProductListApiView, CategoryListApiView
                        )

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('user-list', UserListApiView.as_view(), name='user_list'),
    path('user-create', UserCreateApiView.as_view(), name='user_create'),

    #2
    path('users', UserCreateListApiView.as_view(), name='user-list'),



    path('user-detail/<int:pk>', UserDetailApiView.as_view(), name='user_detail'),
    path('user-update/<int:pk>', UserUpdateApiView.as_view(), name='user_update'),
    path('user-delete/<int:pk>', UserRetrieveAPIView.as_view(), name='user_delete'),

    path('product-list', ProductListApiView.as_view(), name='product_list'),
    path('category-list', CategoryListApiView.as_view(), name='category_list'),

]
