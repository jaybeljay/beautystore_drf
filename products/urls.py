from django.urls import path

from .views import HomeProductListView, ProductCategoryListView, ProductViewSet, SearchView

urlpatterns = [
    path('', HomeProductListView.as_view()),
    path('product/', ProductViewSet.as_view({'get': 'list'})),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name="product_detail"),
    path('product/search/', SearchView.as_view(), name="filter"),
    path('product/search/<slug:slug>/', ProductCategoryListView.as_view(), name="product_category_url"),
]
