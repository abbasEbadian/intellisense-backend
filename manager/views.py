
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ManagerSerializer
from .models import Manager


class MangerViewSet(viewsets.ModelViewSet):
    
    queryset = Manager.objects.all().order_by('-created')
    serializer_class = ManagerSerializer
    permission_classes = [permissions.AllowAny]

