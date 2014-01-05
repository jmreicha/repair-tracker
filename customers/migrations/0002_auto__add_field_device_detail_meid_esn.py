# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'device_detail.meid_esn'
        db.add_column(u'customers_device_detail', 'meid_esn',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'device_detail.meid_esn'
        db.delete_column(u'customers_device_detail', 'meid_esn')


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
            'meid_esn': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
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