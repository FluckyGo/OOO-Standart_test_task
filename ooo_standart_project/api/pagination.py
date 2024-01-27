from rest_framework.pagination import PageNumberPagination

from .constants import PAGINATION_PAGE_SIZE


class RequestPagination(PageNumberPagination):
    """ Пагинация для заявок и реквизитов. """

    page_size = PAGINATION_PAGE_SIZE
    page_size_query_param = 'limit'
