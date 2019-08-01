from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from core.models import Item
from .serializers import ItemListSerializer, ItemDetailSerializer, ItemCreateUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.db.models import Q
from rest_framework import generics, viewsets
from .permissions import IsOwnerorReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .paginations import ItemLimitOffsetPagination, ItemPageNumberPagination


class ItemListAPIView(ListAPIView):
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'slug']
    pagination_class = ItemLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Item.objects.all()
        query = self.request .GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(slug__icontains=query)
            ).distinct()
        return queryset_list


class ItemDetailAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'slug'


class ItemUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerorReadOnly]


class ItemDeleteAPIView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'slug'


class ItemCreateAPIView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# class ItemViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Item.objects.all()
#         serializer_class = ItemSerializer
