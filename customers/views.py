
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound

from customers.helpers import get_cust_last_name, get_cust_first_name
from customers.models import Customer

def index(request):
    #return HttpResponse("Filler index page for the customers view")
    return render_to_response('customers/index.html')

def customer_detail(request, last_name=None):
    """
    Render the view of a customer.

    :param last_name: The last name of a customer
    :type last_name: str

    """
    # Look up a customer object by the last name passed in the URL
    customer = get_cust_last_name(last_name)

    # Build the context dictionary to pass to the template
    context = {
        'cust': customer,
    }

    # This is cool
    return render_to_response('customers/customer.html', context)
