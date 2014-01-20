from django.contrib import admin
from customers.models import Customer, RepairDetail, DeviceDetail

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('pk', 'first_name', 'last_name', 'phone_number', 'address',
	'city', 'state', 'zip_code', 'email')

	search_fields = ['first_name']

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('device_make', 'device_model', 'model_number', 'meid_esn',
	'carrier')

class RepairAdmin(admin.ModelAdmin):
	list_display = ('pk', 'customer_repair', 'device_repair', 'repair_status', 'repair_date',
	'problem_description', 'repair_total')

	list_filter = ['repair_date']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(RepairDetail, RepairAdmin)
admin.site.register(DeviceDetail, DeviceAdmin)
