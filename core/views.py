from django.shortcuts import render
from api.models import SystemInfo

def home(request):
    systems = SystemInfo.objects.filter().values_list('ip_address', 'username').distinct()
    context={
        "systems":systems
    }
    return render(request, "core/home.html", context=context)

def unique_ip(request, ip):
    systems = SystemInfo.objects.filter(ip_address=ip)

    print(ip)
    context={
        "systems":systems
    }
    return render(request, "core/u_ip.html", context=context)
