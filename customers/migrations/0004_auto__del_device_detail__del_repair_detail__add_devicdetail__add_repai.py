# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'device_detail'
        db.delete_table(u'customers_device_detail')

        # Deleting model 'repair_detail'
        db.delete_table(u'customers_repair_detail')

        # Adding model 'DevicDetail'
        db.create_table(u'customers_devicdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('carrier', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('meid_esn', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'customers', ['DevicDetail'])

        # Adding model 'RepairDetail'
        db.create_table(u'customers_repairdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_repair', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Customer'])),
            ('referral_source', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('repair_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('repair_problem_description', self.gf('django.db.models.fields.TextField')(max_length=254)),
            ('repair_notes', self.gf('django.db.models.fields.TextField')(max_length=254)),
            ('repair_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('repair_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'customers', ['RepairDetail'])

        # Deleting field 'customer.customer_address'
        db.delete_column(u'customers_customer', 'customer_address')

        # Deleting field 'customer.customer_email'
        db.delete_column(u'customers_customer', 'customer_email')

        # Deleting field 'customer.customer_last_name'
        db.delete_column(u'customers_customer', 'customer_last_name')

        # Deleting field 'customer.customer_first_name'
        db.delete_column(u'customers_customer', 'customer_first_name')

        # Deleting field 'customer.customer_city'
        db.delete_column(u'customers_customer', 'customer_city')

        # Deleting field 'customer.customer_state'
        db.delete_column(u'customers_customer', 'customer_state')

        # Deleting field 'customer.customer_phone_number'
        db.delete_column(u'customers_customer', 'customer_phone_number')

        # Adding field 'Customer.first_name'
        db.add_column(u'customers_customer', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'Customer.last_name'
        db.add_column(u'customers_customer', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'Customer.phone_number'
        db.add_column(u'customers_customer', 'phone_number',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Customer.address'
        db.add_column(u'customers_customer', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'Customer.city'
        db.add_column(u'customers_customer', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'Customer.state'
        db.add_column(u'customers_customer', 'state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16),
                      keep_default=False)

        # Adding field 'Customer.email'
        db.add_column(u'customers_customer', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=64),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'device_detail'
        db.create_table(u'customers_device_detail', (
            ('make', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('carrier', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meid_esn', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'customers', ['device_detail'])

        # Adding model 'repair_detail'
        db.create_table(u'customers_repair_detail', (
            ('repair_problem_description', self.gf('django.db.models.fields.TextField')(max_length=254)),
            ('customer_repair', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.customer'])),
            ('repair_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('referral_source', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('repair_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('repair_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('repair_notes', self.gf('django.db.models.fields.TextField')(max_length=254)),
        ))
        db.send_create_signal(u'customers', ['repair_detail'])

        # Deleting model 'DevicDetail'
        db.delete_table(u'customers_devicdetail')

        # Deleting model 'RepairDetail'
        db.delete_table(u'customers_repairdetail')

        # Adding field 'customer.customer_address'
        db.add_column(u'customers_customer', 'customer_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'customer.customer_email'
        db.add_column(u'customers_customer', 'customer_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'customer.customer_last_name'
        db.add_column(u'customers_customer', 'customer_last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'customer.customer_first_name'
        db.add_column(u'customers_customer', 'customer_first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'customer.customer_city'
        db.add_column(u'customers_customer', 'customer_city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)

        # Adding field 'customer.customer_state'
        db.add_column(u'customers_customer', 'customer_state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16),
                      keep_default=False)

        # Adding field 'customer.customer_phone_number'
        db.add_column(u'customers_customer', 'customer_phone_number',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Customer.first_name'
        db.delete_column(u'customers_customer', 'first_name')

        # Deleting field 'Customer.last_name'
        db.delete_column(u'customers_customer', 'last_name')

        # Deleting field 'Customer.phone_number'
        db.delete_column(u'customers_customer', 'phone_number')

        # Deleting field 'Customer.address'
        db.delete_column(u'customers_customer', 'address')

        # Deleting field 'Customer.city'
        db.delete_column(u'customers_customer', 'city')

        # Deleting field 'Customer.state'
        db.delete_column(u'customers_customer', 'state')

        # Deleting field 'Customer.email'
        db.delete_column(u'customers_customer', 'email')


    models = {
        u'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '64'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'phone_number': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'customers.devicdetail': {
            'Meta': {'object_name': 'DevicDetail'},
            'carrier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'meid_esn': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'customers.repairdetail': {
            'Meta': {'object_name': 'RepairDetail'},
            'customer_repair': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'referral_source': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'repair_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'repair_date': ('django.db.models.fields.DateTimeField', [], {}),
            'repair_notes': ('django.db.models.fields.TextField', [], {'max_length': '254'}),
            'repair_problem_description': ('django.db.models.fields.TextField', [], {'max_length': '254'}),
            'repair_total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['customers']