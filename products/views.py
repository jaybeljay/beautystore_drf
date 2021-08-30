from django.db import models
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductCategory, Product
from .serializers import ProductCategorySerializer, ProductSerializer, ProductFilterSerializer
from .services import ProductFilter


class HomeProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_active=True).annotate(
            is_favorite=models.Case(
                models.When(favorites__user=request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
        ).order_by('-created')[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductCategoryView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductCategoryListView(APIView):
    def get(self, request, slug):
        products = Product.objects.filter(is_active=True).filter(category__slug=slug).annotate(
            is_favorite=models.Case(
                models.When(favorites__user=request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.filter(is_active=True).annotate(
            is_favorite=models.Case(
                models.When(favorites__user=request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
        )
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        queryset = Product.objects.annotate(
            is_favorite=models.Case(
                models.When(favorites__user=request.user, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
        ).get(pk=pk, is_active=True)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)


class SearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFilterSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
