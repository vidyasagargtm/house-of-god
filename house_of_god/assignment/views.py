from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import models
from . import serializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 10


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(
            post_id__gte=1, post_id__lte=500
        ).values('post_id', 'timestamp').distinct()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
