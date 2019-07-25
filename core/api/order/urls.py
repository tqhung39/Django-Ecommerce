from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import(
    OrderDetailAPIView,
    OrderCreateAPIView,
    OrderListAPIView,
    OrderUpdateAPIView,
    OrderDeleteAPIView,
)

urlpatterns = [
    url(r'^$', OrderListAPIView.as_view(), name='list'),
    url(r'^create/$', OrderCreateAPIView.as_view(), name='create'),
    url(r'^(?P<shipping_address>[\w-]+)/$',
        OrderDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<shipping_address>[\w-]+)/edit/$',
        OrderUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<shipping_address>[\w-]+)/delete/$',
        OrderDeleteAPIView.as_view(), name='delete'),

]
