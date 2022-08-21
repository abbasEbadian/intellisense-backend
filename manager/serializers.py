from os import defpath
from .models import Manager
from rest_framework import serializers


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
        depth = 1


