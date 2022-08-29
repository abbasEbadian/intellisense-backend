
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import CenterSerializer, FAQSerializer, RoadmapSerializer, UtilSerializer
from .models import CenterSlider, Roadmap, Util, FAQ


class RoadmapViewSet(viewsets.ModelViewSet):
    
    queryset = Roadmap.objects.all().order_by('sequence')
    serializer_class = RoadmapSerializer
    permission_classes = [permissions.AllowAny]



class UtilViewSet(viewsets.ModelViewSet):
    
    queryset = Util.objects.all().order_by('sequence')
    serializer_class = UtilSerializer
    permission_classes = [permissions.AllowAny]
class CenterViewSet(viewsets.ModelViewSet):
    
    queryset = CenterSlider.objects.all()
    serializer_class = CenterSerializer
    permission_classes = [permissions.AllowAny]
    

class FAQViewSet(viewsets.ModelViewSet):
    
    queryset = FAQ.objects.all().order_by('sequence')
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = FAQ.objects.filter(active = True)
        serializer = FAQSerializer(queryset, many=True)
        return Response(serializer.data)





