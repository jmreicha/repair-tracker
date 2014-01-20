# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Customer.zip_code'
        db.add_column(u'customers_customer', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(default='50112', max_length=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Customer.zip_code'
        db.delete_column(u'customers_customer', 'zip_code')


    models = {
        u'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '64', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'phone_number': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('localflavor.us.models.USStateField', [], {'default': "'IA'", 'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "'50112'", 'max_length': '5'})
        },
        u'customers.devicedetail': {
            'Meta': {'object_name': 'DeviceDetail'},
            'carrier': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'device_make': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'device_model': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meid_esn': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'model_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        u'customers.repairdetail': {
            'Meta': {'object_name': 'RepairDetail'},
            'customer_repair': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Customer']"}),
            'device_repair': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.DeviceDetail']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'problem_description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'referral_source': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'repair_date': ('django.db.models.fields.DateField', [], {}),
            'repair_status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'repair_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2', 'blank': 'True'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['customers']