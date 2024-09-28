from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

from apps.views import (UserListApiView, UserCreateApiView,
                        UserDetailApiView, UserUpdateApiView,
                        UserRetrieveAPIView, UserCreateListApiView, ProductListApiView, CategoryListApiView
                        )


urlpatterns = [

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    path('admin/', admin.site.urls),

    # #1
    # path('users/', UserListApiView.as_view(), name='user_list'),
    # path('user-create/', UserCreateApiView.as_view(), name='user_create'),

    #2
    # path('users', UserCreateListApiView.as_view(), name='user-list'),



    # path('user-detail/<int:pk>/', UserDetailApiView.as_view(), name='user_detail'),
    # path('user-update/<int:pk>/', UserUpdateApiView.as_view(), name='user_update'),
    # path('user-delete/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_delete'),

    path('products', ProductListApiView.as_view(), name='product_list'),
    path('category-list', CategoryListApiView.as_view(), name='category_list'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),

]
