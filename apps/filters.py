from django.contrib.auth.models import User
from django_filters import FilterSet, NumberFilter


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="id", lookup_expr='gte')
    max_price = NumberFilter(field_name="id", lookup_expr='lte')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']