from django.urls import path
from .import views

urlpatterns = [
   path("", views.home,name="home"),
   path("<str:ip>/", views.unique_ip,name="u_ip"),
]
