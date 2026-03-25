from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import IsAuthorOrReadOnly

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

