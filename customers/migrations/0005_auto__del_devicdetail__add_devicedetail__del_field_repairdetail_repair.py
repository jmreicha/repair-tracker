# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DevicDetail'
        db.delete_table(u'customers_devicdetail')

        # Adding model 'DeviceDetail'
        db.create_table(u'customers_devicedetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('carrier', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('meid_esn', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'customers', ['DeviceDetail'])

        # Deleting field 'RepairDetail.repair_problem_description'
        db.delete_column(u'customers_repairdetail', 'repair_problem_description')

        # Deleting field 'RepairDetail.repair_total'
        db.delete_column(u'customers_repairdetail', 'repair_total')

        # Deleting field 'RepairDetail.repair_cost'
        db.delete_column(u'customers_repairdetail', 'repair_cost')

        # Deleting field 'RepairDetail.repair_notes'
        db.delete_column(u'customers_repairdetail', 'repair_notes')

        # Adding field 'RepairDetail.problem_description'
        db.add_column(u'customers_repairdetail', 'problem_description',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=254),
                      keep_default=False)

        # Adding field 'RepairDetail.notes'
        db.add_column(u'customers_repairdetail', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=254),
                      keep_default=False)

        # Adding field 'RepairDetail.cost'
        db.add_column(u'customers_repairdetail', 'cost',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'RepairDetail.total'
        db.add_column(u'customers_repairdetail', 'total',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'DevicDetail'
        db.create_table(u'customers_devicdetail', (
            ('make', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('carrier', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=64)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meid_esn', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'customers', ['DevicDetail'])

        # Deleting model 'DeviceDetail'
        db.delete_table(u'customers_devicedetail')

        # Adding field 'RepairDetail.repair_problem_description'
        db.add_column(u'customers_repairdetail', 'repair_problem_description',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=254),
                      keep_default=False)

        # Adding field 'RepairDetail.repair_total'
        db.add_column(u'customers_repairdetail', 'repair_total',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'RepairDetail.repair_cost'
        db.add_column(u'customers_repairdetail', 'repair_cost',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'RepairDetail.repair_notes'
        db.add_column(u'customers_repairdetail', 'repair_notes',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=254),
                      keep_default=False)

        # Deleting field 'RepairDetail.problem_description'
        db.delete_column(u'customers_repairdetail', 'problem_description')

        # Deleting field 'RepairDetail.notes'
        db.delete_column(u'customers_repairdetail', 'notes')

        # Deleting field 'RepairDetail.cost'
        db.delete_column(u'customers_repairdetail', 'cost')

        # Deleting field 'RepairDetail.total'
        db.delete_column(u'customers_repairdetail', 'total')


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
        u'customers.devicedetail': {
            'Meta': {'object_name': 'DeviceDetail'},
            'carrier': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'meid_esn': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'customers.repairdetail': {
            'Meta': {'object_name': 'RepairDetail'},
            'cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'customer_repair': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['customers.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '254'}),
            'problem_description': ('django.db.models.fields.TextField', [], {'max_length': '254'}),
            'referral_source': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'repair_date': ('django.db.models.fields.DateTimeField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['customers']