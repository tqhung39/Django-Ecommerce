from django.urls import path, include
from . import views
from django.conf.urls import url
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    AddReviewView,
    # GeneratePDF
)
from .views import searchbook
app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('search/', views.searchbook, name='search'),
    path('review/', views.review_list, name='review_list'),
    path('product/<slug>/add-review', AddReviewView, name='add_review'),
    # url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),

]
