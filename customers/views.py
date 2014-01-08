
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
	return HttpResponse("Hello world.  This is the index page.")

def customer_detail(request, last_name):
	return HttpResponse("You are looking at customer name: %s " % last_name)	
