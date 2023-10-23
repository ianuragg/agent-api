from django.urls import path
from .views import SystemInfoList, SystemInfoDetail


#Endpoints
# /systeminfo/
# /systeminfo/<pk>

urlpatterns = [
   #API Endpoints
   path("systeminfo/", SystemInfoList.as_view()),
   path("systeminfo/<int:pk>/", SystemInfoDetail.as_view()),
]
