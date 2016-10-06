# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Instance', fields ['extractionPropertyID', 'entityID']
        db.delete_unique('crawler_instance', ['extractionPropertyID_id', 'entityID_id'])

        # Deleting model 'Instance'
        db.delete_table('crawler_instance')

        # Adding model 'Property'
        db.create_table('crawler_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('extractionPropertyID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('entityID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionEntity'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('crawler', ['Property'])

        # Adding unique constraint on 'Property', fields ['extractionPropertyID', 'entityID']
        db.create_unique('crawler_property', ['extractionPropertyID_id', 'entityID_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Property', fields ['extractionPropertyID', 'entityID']
        db.delete_unique('crawler_property', ['extractionPropertyID_id', 'entityID_id'])

        # Adding model 'Instance'
        db.create_table('crawler_instance', (
            ('extractionPropertyID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entityID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionEntity'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('crawler', ['Instance'])

        # Adding unique constraint on 'Instance', fields ['extractionPropertyID', 'entityID']
        db.create_unique('crawler_instance', ['extractionPropertyID_id', 'entityID_id'])

        # Deleting model 'Property'
        db.delete_table('crawler_property')


    models = {
        'crawler.crawlproperty': {
            'Meta': {'object_name': 'CrawlProperty', 'ordering': "['websiteID', 'url']", 'unique_together': "(('websiteID', 'url'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nJobs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'page404Path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionentity': {
            'Meta': {'object_name': 'ExtractionEntity', 'ordering': "['websiteID', 'entitySelector']", 'unique_together': "(('websiteID', 'entitySelector'),)"},
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'InstanceCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'ExtractionProperty'},
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'getFromAttribute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanceSelector': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'splitDataFormate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.property': {
            'Meta': {'object_name': 'Property', 'ordering': "['extractionPropertyID', 'entityID']", 'unique_together': "(('extractionPropertyID', 'entityID'),)"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'entityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'extractionPropertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.website': {
            'Extracted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'Website'},
            'canExtract': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'checkDataset': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datasetFileNum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'datasetLocation': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True', 'null': 'True'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']