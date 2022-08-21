
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RoadmapSerializer, UtilSerializer
from .models import Roadmap,Util


class RoadmapViewSet(viewsets.ModelViewSet):
    
    queryset = Roadmap.objects.all().order_by('-created')
    serializer_class = RoadmapSerializer
    permission_classes = [permissions.AllowAny]



class UtilViewSet(viewsets.ModelViewSet):
    
    queryset = Util.objects.all().order_by('-created')
    serializer_class = UtilSerializer
    permission_classes = [permissions.AllowAny]


