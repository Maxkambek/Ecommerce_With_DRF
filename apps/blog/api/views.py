from rest_framework import permissions
from ..models import Post, Tag
from ..serializers import TagSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import generics, status


class TagListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/blog/tag/list/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/tag/blog/create/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/blog/tag/rud/{pk}
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/blog/post/list/
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/blog/post/create/
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/blog/post/rud/{id}
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]