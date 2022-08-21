from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BlogSerializer,  BlogCategorySerializer
from .models import Blog, BlogCategory


class BlogViewSet(viewsets.ModelViewSet):
    
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]


class BlogCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = BlogCategory.objects.all().order_by('-created')
    serializer_class = BlogCategorySerializer
    permission_classes = [permissions.AllowAny]
