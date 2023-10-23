from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SystemInfoSerializer
from .models import SystemInfo
from rest_framework import generics

#SystemInfo List View
class SystemInfoList(generics.ListCreateAPIView):
    queryset = SystemInfo.objects.all()
    serializer_class = SystemInfoSerializer

#SystemInfo Detail View
class SystemInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystemInfo.objects.all()
    serializer_class = SystemInfoSerializer