from django.db import models

# Create your models here.

class Customer(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	phone_number = models.BigIntegerField(default=0)
	address = models.CharField(max_length=64)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=16)
	email = models.EmailField(max_length=64)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class RepairDetail(models.Model):
	customer_repair = models.ForeignKey(Customer)
	referral_source = models.CharField(max_length=64)
	repair_date = models.DateTimeField("Date")
	problem_description = models.TextField(max_length=254)
	notes = models.TextField(max_length=254)
	cost = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	
	def __str__(self):
		return self.customer_repair

class DeviceDetail(models.Model):
	make = models.CharField(max_length=64)
	model = models.CharField(max_length=64)
	carrier = models.CharField(max_length=64)
	meid_esn = models.CharField(max_length=64)

	def __str__(self):
		return self.model
