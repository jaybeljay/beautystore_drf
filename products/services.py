from django_filters import rest_framework as filters

from .models import ProductCategory, Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    price = filters.RangeFilter()
    category = filters.ModelChoiceFilter(queryset=ProductCategory.objects.all())
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']
