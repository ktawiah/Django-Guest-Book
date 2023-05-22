from django.shortcuts import render
from rest_framework import viewsets
from guest_book_app.models import Comment
from .serializers import CommentSerializer
from rest_framework import filters


class CommentViewsets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("name",)
    ordering_fields = (
        "name",
        "id",
    )
