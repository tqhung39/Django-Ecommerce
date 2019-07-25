from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import(
    CouponDetailAPIView,
    CouponCreateAPIView,
    CouponListAPIView,
    CouponUpdateAPIView,
    CouponDeleteAPIView,
)

urlpatterns = [
    url(r'^$', CouponListAPIView.as_view(), name='list'),
    url(r'^create/$', CouponCreateAPIView.as_view(), name='create'),
    url(r'^(?P<code>[\w-]+)/$', CouponDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<code>[\w-]+)/edit/$',
        CouponUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<code>[\w-]+)/delete/$',
        CouponDeleteAPIView.as_view(), name='delete'),
]
