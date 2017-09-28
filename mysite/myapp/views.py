from django.shortcuts import render
from django.http import Http404
from . models import GPU, CPU, RAM, PS


def index(request):
    try:
        best_gpu = GPU.objects.order_by('-hashing_rate')
        best_cpu = CPU.objects.order_by('-cost')
        best_ram = RAM.objects.order_by('-cost')
        best_ps = PS.objects.order_by('-cost')

    except GPU.objects.DoesNotExist:
        raise Http404("No GPU exists")

    return render(request, 'myapp/index.html', {'gpu': best_gpu, 'cpu': best_cpu, 'ram': best_ram, 'ps': best_ps})


def detail(request):
    try:
        selected_gpu = request.POST['GPU_name']
        best_gpu = GPU.objects.order_by('-hashing_rate')
        best_cpu = CPU.objects.order_by('-cost')
        best_ram = RAM.objects.order_by('-cost')
        best_ps = PS.objects.order_by('-cost')
        sg = GPU.objects.filter(name=selected_gpu)
    except request.POST['GPU_name'].DoesNotExist:
        return render(request, 'myapp/index.html', {
            'gpu': best_gpu, 'cpu': best_cpu, 'ram': best_ram, 'ps': best_ps,
            'error_message': "Invalid input",
        })
    else:
        return render(request, 'myapp/index.html', {'gpu': best_gpu, 'cpu': best_cpu, 'ram': best_ram, 'ps': best_ps,
                                                    'result': sg.hashing_rate})

