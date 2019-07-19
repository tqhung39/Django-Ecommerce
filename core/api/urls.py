from django.conf.urls import url
from django.contrib import admin
from .views import(
    ItemDetailAPIView,
    ItemCreateAPIView,
    ItemListAPIView,
    ItemUpdateAPIView,
    ItemDeleteAPIView
)

urlpatterns = [
    url(r'^$', ItemListAPIView.as_view(), name='list'),
    url(r'^create/$', ItemCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ItemDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$',
        ItemUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$',
        ItemDeleteAPIView.as_view(), name='delete'),
]
