
from django.db import models
from localflavor.us.models import PhoneNumberField
from localflavor.us.models import USStateField
from django.utils.translation import ugettext_lazy as _


class Customer(models.Model):
	"""Defines a customer object."""
	first_name = models.CharField(_('First Name'), max_length=64)
	last_name = models.CharField(_('Last Name'), max_length=64)
	phone_number = PhoneNumberField()
	address = models.CharField(_('Address'), max_length=64, blank=True)
	city = models.CharField(_('City'), max_length=64, blank=True)
	state = USStateField(default='IA')
	zip_code = models.CharField(_("Zip Code"), max_length=5, default="50112")
	email = models.EmailField(max_length=64, blank=True)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)


class DeviceDetail(models.Model):
	"""Defines a Device Detail object."""
	device_make = models.CharField(_('Make'), max_length=64)
	device_model = models.CharField(_('Model'), max_length=64)
	#device_customer = models.ForeignKey(Customer)
	model_number = models.CharField(
        _('Model Number'), max_length=32, blank=True)
	carrier = models.CharField(_('Carrier'), max_length=64, blank=True)
	meid_esn = models.CharField(_('MEID/ESN'), max_length=64, blank=True)

	def __unicode__(self):
		return u'%s %s' % (self.device_make, self.device_model)


class RepairDetail(models.Model):
	"""Defines a Repair Detail object."""
	customer_repair = models.ForeignKey(Customer)
	device_repair = models.ForeignKey(DeviceDetail, null=True)
	referral_source = models.CharField(
        _('Referral Source'),
        max_length=64,
        blank=True
        )
	repair_date = models.DateField("Date")
	problem_description = models.TextField(
        _('Problem Description'),
        max_length=255
        )
	notes = models.TextField(_('Repair Notes'), max_length=255, blank=True)

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

	total_cost = models.DecimalField(
        _('Cost ($)'),
         max_digits=16,
         decimal_places=2,
         blank=True
         )
	repair_total = models.DecimalField(
        _('Total ($)'),
         max_digits=16,
         decimal_places=2,
         blank=True
         )
	def __unicode__(self):
		return u"{} {}".format(self.customer_repair, self.problem_description)

