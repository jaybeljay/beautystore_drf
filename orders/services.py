from django_filters import rest_framework as filters

from .models import ProductInCart


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductInCartFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='product__category__name', lookup_expr='in')
    price_per_item = filters.RangeFilter()
    
    class Meta:
        model = ProductInCart
        fields = ['product__category', 'price_per_item']
