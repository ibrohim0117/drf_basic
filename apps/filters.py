from django.contrib.auth.models import User
from django_filters import FilterSet, NumberFilter, CharFilter

from apps.models import Product


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="id", lookup_expr='gte')
    max_price = NumberFilter(field_name="id", lookup_expr='lte')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProductFilterSet(FilterSet):
    # description = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = 'name', 'description'