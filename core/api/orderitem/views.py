from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from core.models import OrderItem
from .serializers import OrderItemCreateUpdateSerializer, OrderItemDetailSerializer, OrderItemListSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .paginations import OrderItemLimitOffsetPagination, OrderItemPageNumberPagination
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter


class OrderItemListAPIView(ListAPIView):
    serializer_class = OrderItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item', 'quantity']
    pagination_class = OrderItemLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = OrderItem.objects.all()
        query = self.request .GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(item__icontains=query) |
                Q(quantity__icontains=query)
            ).distinct()
        return queryset_list


class OrderItemDetailAPIView(RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemDetailSerializer
    lookup_field = 'user'


class OrderItemUpdateAPIView(RetrieveUpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateUpdateSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderItemDeleteAPIView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemDetailSerializer
    lookup_field = 'user'


class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
