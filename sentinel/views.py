import psutil
import platform
from datetime import datetime
from django.shortcuts import render
from urllib3 import request

def dashboard(request):
    # System stats
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    network = psutil.net_io_counters()

    # User stats
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    ip_address = request.META.get('REMOTE_ADDR')

    # Convert bytes to MB for better readability
    sent_mb = round(network.bytes_sent / (1024 * 1024), 2)
    recv_mb = round(network.bytes_recv / (1024 * 1024), 2)
    
    # Calculate Uptime
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    
    context = {
        'cpu': cpu_usage,
        'ram_percent': memory.percent,
        'ram_used': round(memory.used / (1024**3), 2),
        'ram_total': round(memory.total / (1024**3), 2),
        'disk_percent': disk.percent,
        'uptime': str(uptime).split('.')[0],
        'os': platform.system(),
        'processor': platform.processor(),
        'user_browser': user_agent,
        'user_ip': ip_address,
        'net_sent': sent_mb,
        'net_recv': recv_mb,
    }
    return render(request, 'sentinel/dashboard.html', context)
