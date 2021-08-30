from django.urls import path

from .views import ProductInCartViewSet, FavoriteProductView, OrderView, ProductInOrderView


product_in_cart_list = ProductInCartViewSet.as_view({
    'get': 'list',
    'post': 'add_to_cart'
})

product_in_cart_detail = ProductInCartViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

favorite_product_list = FavoriteProductView.as_view({
    'get': 'list',
    'post': 'add_to_favorites'
})

favorite_product_detail = FavoriteProductView.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

order_list = OrderView.as_view({
    'get': 'list',
    'post': 'create_order',
})

product_in_order_list = ProductInOrderView.as_view({
    'get': 'list'
})

product_in_order_detail = ProductInOrderView.as_view({
    'get': 'retrieve',
})


urlpatterns = [
    path('cart/', product_in_cart_list, name='cart'),
    path('cart/<int:pk>/', product_in_cart_detail, name='product_in_cart'),
    path('favorites/', favorite_product_list, name='favorites'),
    path('favorites/<int:pk>/', favorite_product_detail, name='favorite_product'),
    path('orders/', order_list, name='orders'),
    path('orders/<int:order_id>/', product_in_order_list, name='order'),
    path('orders/<int:order_id>/<int:pk>/', product_in_order_detail, name='product_in_order'),
]
