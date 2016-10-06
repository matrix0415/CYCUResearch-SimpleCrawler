# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Website.datasetLocation'
        db.add_column('crawler_website', 'datasetLocation',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=150),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Website.datasetLocation'
        db.delete_column('crawler_website', 'datasetLocation')


    models = {
        'crawler.crawlproperty': {
            'Meta': {'object_name': 'CrawlProperty', 'ordering': "['websiteID', 'url']", 'unique_together': "(('websiteID', 'url'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nJobs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'page404Path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.entity': {
            'Meta': {'object_name': 'Entity', 'ordering': "['websiteID', 'path', 'entitySelector']"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'entitySelector': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'InstanceCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'ExtractionProperty'},
            'entitySelector': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'getFromAttribute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanceSelector': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'splitDataFormate': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.instance': {
            'Meta': {'object_name': 'Instance', 'ordering': "['extractionPropertyID', 'entityID']", 'unique_together': "(('extractionPropertyID', 'entityID'),)"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'entityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Entity']"}),
            'extractionPropertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.website': {
            'Extracted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'Website'},
            'canExtract': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'checkDataset': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datasetLocation': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '150'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']