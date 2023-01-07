from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'phone_number', 'device_name', 'customer_mail', 'customer_type', 'submitted_price', 'date_submitted', 'device_state', 'device_problem']

admin.site.register(Service, ServiceAdmin)