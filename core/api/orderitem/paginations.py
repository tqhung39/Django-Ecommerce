from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class OrderItemLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5


class OrderItemPageNumberPagination(PageNumberPagination):
    page_size = 10
