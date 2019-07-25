from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class CouponLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5


class CouponPageNumberPagination(PageNumberPagination):
    page_size = 10
