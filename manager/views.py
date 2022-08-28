

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ManagerSerializer
from .models import Manager
from rest_framework.response import Response


class MangerViewSet(viewsets.ModelViewSet):
    
    queryset = Manager.objects.all().order_by('-created')
    serializer_class = ManagerSerializer
    permission_classes = [permissions.AllowAny]
    
    def list(self, request):
        page = request.GET.get('page', 'all')
        queryset = Manager.objects.all()
        queryset = [x for x in queryset if 'all' in x.corresponding_page or page in x.corresponding_page ]
        serializer = ManagerSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

