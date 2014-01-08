
from django.db import models


class Customer(models.Model):
	"""Defines a customer object."""
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	phone_number = models.BigIntegerField(default=0, blank=True)
	address = models.CharField(max_length=64, blank=True)
	city = models.CharField(max_length=64, blank=True)
	state = models.CharField(max_length=16, blank=True)
	zip_code = models.IntegerField(max_length=8, blank=True)
	email = models.EmailField(max_length=64, blank=True)
	
	def __unicode__(self):
		return u'%s %s %s' % (self.pk, self.first_name, self.last_name)


class DeviceDetail(models.Model):
	"""Defines a Device Detail object."""
	device_make = models.CharField(max_length=64)
	device_model = models.CharField(max_length=64)
	#device_customer = models.ForeignKey(Customer)
	model_number = models.CharField(max_length=32, blank=True)
	carrier = models.CharField(max_length=64, blank=True)
	meid_esn = models.CharField(max_length=64, blank=True)

	def __unicode__(self):
		return u'%s %s' % (self.device_make, self.device_model)


class RepairDetail(models.Model):
	"""Defines a Repair Detail object."""
	customer_repair = models.ForeignKey(Customer)
	device_repair = models.ForeignKey(DeviceDetail, null=True)
	referral_source = models.CharField(max_length=64, blank=True)
	repair_date = models.DateField("Date")
	problem_description = models.TextField(max_length=255)
	notes = models.TextField(max_length=255, blank=True)

	STATUS = (
		(("on hold", "On hold")),
		(("waiting on customer", "Waiting on customer")),
		(("purchase ok'd", "Purchase ok'd")),
		(("part purchased", "Part purchased")),
		(("waiting on parts", "Waiting on parts")),
		(("part delivered", "Part delivered")),
		(("appt scheduled", "Appointment scheduled")),
		(("didn't want repair", "Didn't want repair")),
		(("complete", "Complete"))
	)

	repair_status = models.CharField(max_length=16, choices=STATUS)
	total_cost = models.DecimalField(max_digits=16, decimal_places=2, blank=True)
	repair_total = models.DecimalField(max_digits=16, decimal_places=2, blank=True)
	
	def __unicode__(self):
		return u"{} {}".format(self.customer_repair, self.problem_description)

