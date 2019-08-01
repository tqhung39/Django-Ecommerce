from django.urls import path
from .views import (
    ItemListView,
    AddToCartView,
    OrderDetailView
)

urlpatterns = [
    path('product/', ItemListView.as_view(), name='product-list'),
    path('', AddToCartView.as_view(), name='add-to-cart'),
    path('order/', OrderDetailView.as_view(), name='order-summary')
]
