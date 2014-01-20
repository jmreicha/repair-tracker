"""
Helper functions
----------------

This module contains functions that are frequesntly  reused in views.

"""
from customers.models import Customer


def get_cust_last_name(last_name):
	"""
	Return a customer model if it's found, otherwise raise an exception.

	:param last_name: A customer's last name
	:type last_name: str

	"""
	return Customer.objects.get(last_name=last_name)


def get_cust_first_name(first_name):
    return Customer.objects.get(first_name=first_name)


def get_cust_address(address):
    return Customer.objects.get(address)


def get_cust_email(email_address):
    return Customer.objects.get(email_address)


def get_cust_phone(phone_number):
    return Customer.objects.get(phone_number)
