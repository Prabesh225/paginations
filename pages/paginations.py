from rest_framework.pagination import CursorPagination

class myoffsetpagination(CursorPagination):
    page_size =4
    ordering ='id'

# class myoffsetpagination(LimitOffsetPagination):
#     default_limit = 10
#     offset_query_param = 'offset'
#     last_page_strings = ['last']
#     page_query_param = 'p'
#     max_limit = 4


# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#     last_page_strings = ['last']
#     page_query_param = 'p'