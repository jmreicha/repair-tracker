from django.contrib import admin
from customers.models import Customer,RepairDetail, DeviceDetail

# Register your models here.

admin.site.register(Customer)
admin.site.register(RepairDetail)
admin.site.register(DeviceDetail)
