from rest_framework import serializers

from .models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    category_url = serializers.URLField(source="get_absolute_url")
    
    class Meta:
        model = ProductCategory
        fields = ['name', 'slug', 'category_url']


class ProductSerializer(serializers.ModelSerializer):
    category_slug = serializers.CharField(source="category.slug", read_only=True)
    is_favorite = serializers.BooleanField()
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount', 'image', 'category_slug', 'is_favorite']


class ProductFilterSerializer(serializers.ModelSerializer):
    category_slug = serializers.CharField(source="category.slug", read_only=True)
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount', 'image', 'category_slug']
