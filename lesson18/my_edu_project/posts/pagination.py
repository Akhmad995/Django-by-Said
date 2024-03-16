from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data) -> Response:
        return Response({
            'post_count': self.page.paginator.count,
            'posts': data
        })
