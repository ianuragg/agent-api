from rest_framework import serializers
from .models import SystemInfo

#SystemInfo Serializer
class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfo
        fields = "__all__"