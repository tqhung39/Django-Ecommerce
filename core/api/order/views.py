from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from core.models import Order
from .serializers import OrderCreateUpdateSerializer, OrderDetailSerializer, OrderListSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import generics
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .paginations import OrderLimitOffsetPagination, OrderPageNumberPagination


class OrderListAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'shipping_address']
    pagination_class = OrderLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Order.objects.all()
        query = self.request .GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(user__icontains=query) |
                Q(shipping_address__icontains=query)
            ).distinct()
        return queryset_list


class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'user'


class OrderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderDeleteAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'user'


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
