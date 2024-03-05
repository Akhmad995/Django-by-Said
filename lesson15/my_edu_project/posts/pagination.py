from rest_framework.pagination import PageNumberPagination

# Пагинация - Pagination

# Классы пашинации
# 1. PageNumberPagination
# http://127.0.0.1:8000/posts/?page=2

# 2. LimitOffsetPagination
# http://127.0.0.1:8000/posts/?limit=100&offset=400

# 3. CursorPagination
class PostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
