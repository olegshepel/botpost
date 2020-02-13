from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from posts.models import Post
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('id')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def set_like(self, like=None):
        user = self.request.user
        post = self.get_object()
        post.like(user) if like else post.dislike(user)
        serializer = self.get_serializer_class()(post)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        return self.set_like(like=True)

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated])
    def dislike(self, request, pk=None):
        return self.set_like(like=False)
