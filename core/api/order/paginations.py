from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class OrderLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5


class OrderPageNumberPagination(PageNumberPagination):
    page_size = 10
