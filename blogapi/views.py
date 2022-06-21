from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Post
from .serializer import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostList(ListCreateAPIView):
    queryset = Post.objects.filter(status='publish')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status='publish')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
