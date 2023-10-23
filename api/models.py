from django.db import models


#System Information Model
class SystemInfo(models.Model):
    system = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    machine = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    total_memory = models.DecimalField(max_digits=10, decimal_places=2)
    internet_connected = models.BooleanField(default=False)
    installed_apps = models.IntegerField(default=0)
    running_processes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('ip_address',)

    def __str__(self):
        return self.username
