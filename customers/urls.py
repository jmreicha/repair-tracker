from django.conf.urls import patterns, url

from customers import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<last_name>\w+)/$', views.customer_detail, name='customer_detail')
)
