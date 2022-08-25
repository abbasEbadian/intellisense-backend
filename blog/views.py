from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BlogSerializer,  BlogCategorySerializer
from .models import Blog, BlogCategory
from rest_framework.response import Response

class BlogViewSet(viewsets.ModelViewSet):
    
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)



class BlogCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = BlogCategory.objects.all().order_by('-created')
    serializer_class = BlogCategorySerializer
    permission_classes = [permissions.AllowAny]
