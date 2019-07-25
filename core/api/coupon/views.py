from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from core.models import Coupon
from .serializers import CouponCreateUpdateSerializer, CouponDetailSerializer, CouponListSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .paginations import CouponLimitOffsetPagination, CouponPageNumberPagination


class CouponListAPIView(ListAPIView):
    serializer_class = CouponListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['code', 'amount']
    pagination_class = CouponLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Coupon.objects.all()
        query = self.request .GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(code__icontains=query) |
                Q(amount__icontains=query)
            ).distinct()
        return queryset_list


class CouponDetailAPIView(RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponDetailSerializer
    lookup_field = 'code'


class CouponUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponCreateUpdateSerializer
    lookup_field = 'code'
    permission_classes = [IsAuthenticatedOrReadOnly]


class CouponDeleteAPIView(DestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponDetailSerializer
    lookup_field = 'code'


class CouponCreateAPIView(CreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
