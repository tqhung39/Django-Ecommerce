from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import(
    OrderItemDetailAPIView,
    OrderItemCreateAPIView,
    OrderItemListAPIView,
    OrderItemUpdateAPIView,
    OrderItemDeleteAPIView,
)

urlpatterns = [
    url(r'^$', OrderItemListAPIView.as_view(), name='list'),
    url(r'^create/$', OrderItemCreateAPIView.as_view(), name='create'),
    url(r'^(?P<user>[\w-]+)/$',
        OrderItemDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<user>[\w-]+)/edit/$',
        OrderItemUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<user>[\w-]+)/delete/$',
        OrderItemDeleteAPIView.as_view(), name='delete'),
]
