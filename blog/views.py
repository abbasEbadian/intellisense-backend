from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BlogSerializer,  BlogCategorySerializer
from .models import Blog, BlogCategory
from rest_framework.response import Response
from rest_framework.decorators import action

class BlogViewSet(viewsets.ModelViewSet):
    
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        page = request.GET.get('page', 'all')
        nofilter = request.GET.get('nofilter', False) # False means filter by corresponding_page
        if not nofilter:
            queryset = Blog.objects.filter(category_id__title='news')
            queryset = [x for x in queryset if 'all' in x.corresponding_page or page in x.corresponding_page ]
        else:
            queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def press(self, request):
        queryset = Blog.objects.filter(category_id__title='press')
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)



class BlogCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = BlogCategory.objects.all().order_by('-created')
    serializer_class = BlogCategorySerializer
    permission_classes = [permissions.AllowAny]
