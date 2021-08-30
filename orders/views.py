from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import FavoriteProduct, ProductInCart, Order, ProductInOrder
from .serializers import ProductInCartSerializer, FavoriteProductSerializer, OrderSerializer, ProductInOrderSerializer


class ProductInCartViewSet(viewsets.ModelViewSet):
    serializer_class = ProductInCartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ProductInCart.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def add_to_cart(self, request):
        product_id = request.POST.get('product_id')
        nmb = request.POST.get('nmb')
        new_product, created = ProductInCart.objects.get_or_create(user=request.user, product_id=product_id, defaults={"nmb": nmb})
        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class FavoriteProductView(viewsets.ModelViewSet):
    serializer_class = FavoriteProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def add_to_favorites(self, request):
        product_id = request.POST.get('obj')
        favorite, created = FavoriteProduct.objects.get_or_create(user=request.user, obj_id=product_id)
        if not created:
            favorite.delete()
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class OrderView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def create_order(self, request):
        order = Order.objects.create(
            user=request.user,
            user_first_name=request.POST.get('user_first_name'),
            user_last_name=request.POST.get('user_last_name'),
            user_phone=request.POST.get('user_phone'),
            user_address=request.POST.get('user_address'),
            comments=request.POST.get('comments'),
            status_id=1,
            )
        
        products_in_cart = ProductInCart.objects.filter(user=request.user, is_active=True)
        
        for product in products_in_cart:
            product_in_order = ProductInOrder.objects.create(
                order=order,
                product=product.product,
                nmb=product.nmb,
                price_per_item=product.price_per_item,
                total_price=product.total_price
                )

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductInOrderView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductInOrderSerializer
    
    def get_queryset(self):
        return ProductInOrder.objects.filter(order_id=self.kwargs['order_id'])
