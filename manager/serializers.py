from os import defpath
from .models import Manager
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_superuser', 'is_staff', 'user_permissions', 'groups')

class ManagerSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = Manager
        fields = '__all__'
        depth = 1


