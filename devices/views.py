from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
import subprocess
import socket
# from models import Device

# Create your views here.
def device_list(request):
    devices = Device.objects.all()

    device_status = []
    for d in devices:
        status = ping_device(d.ip_address)
        device_status.append((d, status))
    online_count = sum(1 for _, status in device_status if status)
    offline_count = len(device_status )- online_count

    return render(request, 'devices/list.html', {
        'device_status': device_status, 
        'online_count' : online_count,
        'offline_count' : offline_count,
    })

def ping_device(ip):
    try:
        result = subprocess.run(["ping", "-n", "1", ip], capture_output=True)
        return result.returncode==0
    except:
        return False
    
def add_device(request):
    if request.method == "POST":
        name = request.POST.get('name')
        ip = request.POST.get('ip')
        dtype = request.POST.get('type')
        
        Device.objects.create(
            name = name, 
            ip_address = ip,
            device_type = dtype
        )
        
        return redirect('device_list')
    
    return render(request, 'devices/add.html')

def ip_lookup(request):
    hostname = None
    ip = None
    
    if request.method == "POST":
        ip = request.POST.get('ip')
        
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "NO HOSTNAME FOUND"
            
    return render(request, 'devices/lookup.html', {
        'hostname' : hostname,
        'ip' : ip
    })

def edit_device(request, id):
    device = get_object_or_404(Device, id=id)

    if request.method == "POST":
        device.name = request.POST.get('name')
        device.ip_address = request.POST.get('ip')
        device.device_type = request.POST.get('type')
        device.save()

        return redirect('device_list')

    return render(request, 'devices/edit.html', {'device': device})

def delete_device(request, id):
    device = get_object_or_404(Device, id=id)
    device.delete()
    return redirect('device_list')