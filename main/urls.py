from django.urls import path

from .views import ProfileView

urlpatterns = [
    path('account/<int:pk>/', ProfileView.as_view({'get': 'retrieve'}), name='account'),
    path('account/<int:pk>/edit/', ProfileView.as_view({'patch': 'partial_update'}), name='edit_account'),
    path('account/<int:pk>/delete/', ProfileView.as_view({'delete': 'destroy'}), name='delete_account'),
]
