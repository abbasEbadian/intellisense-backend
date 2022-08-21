
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactSerializer
from .models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all().order_by('-created')
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


