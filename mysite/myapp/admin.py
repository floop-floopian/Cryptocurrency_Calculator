from django.contrib import admin
from .models import GPU, CPU, RAM, PS

# Register your models here.
admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(PS)

