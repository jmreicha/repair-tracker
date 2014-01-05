# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'customer'
        db.create_table(u'customers_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('customer_last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('customer_phone_number', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('customer_address', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('customer_city', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('customer_state', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('customer_email', self.gf('django.db.models.fields.EmailField')(max_length=64)),
        ))
        db.send_create_signal(u'customers', ['customer'])

        # Adding model 'repair_detail'
        db.create_table(u'customers_repair_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_repair', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.customer'])),
            ('referral_source', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('repair_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('repair_problem_description', self.gf('django.db.models.fields.TextField')(max_length=254)),
            ('repair_notes', self.gf('django.db.models.fields.TextField')(max_length=254)),
            ('repair_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('repair_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'customers', ['repair_detail'])

        # Adding model 'device_detail'
        db.create_table(u'customers_device_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('carrier', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'customers', ['device_detail'])


    def backwards(self, orm):
        # Deleting model 'customer'
        db.delete_table(u'customers_customer')

        # Deleting model 'repair_detail'
        db.delete_table(u'customers_repair_detail')

        # Deleting model 'device_detail'
        db.delete_table(u'customers_device_detail')


    models = {
        u'customers.customer': {
            'Meta': {'object_name': 'customer'},
            'customer_address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'customer_city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'customer_email': ('django.db.models.fields.EmailField', [], {'max_length': '64'}),
            'customer_first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'customer_last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'customer_phone_number': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'customer_state': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'customers.device_detail': {
            'Meta': {'object_name': 'device_detail'},
            'carrier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'customers.repair_detail': {
            'Meta': {'object_name': 'repair_detail'},
            'customer_repair': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.customer']"}),
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