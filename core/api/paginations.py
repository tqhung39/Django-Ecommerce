from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ItemLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5


class ItemPageNumberPagination(PageNumberPagination):
    page_size = 10
