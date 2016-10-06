# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ExtractionProperty.getFromAttribute'
        db.add_column('crawler_extractionproperty', 'getFromAttribute',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ExtractionProperty.splitDataFormate'
        db.add_column('crawler_extractionproperty', 'splitDataFormate',
                      self.gf('django.db.models.fields.CharField')(default='123', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ExtractionProperty.getFromAttribute'
        db.delete_column('crawler_extractionproperty', 'getFromAttribute')

        # Deleting field 'ExtractionProperty.splitDataFormate'
        db.delete_column('crawler_extractionproperty', 'splitDataFormate')


    models = {
        'crawler.crawlproperty': {
            'Meta': {'unique_together': "(('websiteID', 'url'),)", 'object_name': 'CrawlProperty', 'ordering': "['websiteID', 'url']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nJobs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'page404Path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionentity': {
            'EntityCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'unique_together': "(('websiteID', 'entitySelector'),)", 'object_name': 'ExtractionEntity', 'ordering': "['websiteID', 'entitySelector']"},
            'entityPath': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'entitySelector': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'Meta': {'unique_together': "(('extractionEntityID', 'propertySelector'),)", 'object_name': 'ExtractionProperty', 'ordering': "['extractionEntityID', 'propertySelector']"},
            'PropertyCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'getFromAttribute': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'propertySelector': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'splitDataFormate': ('django.db.models.fields.CharField', [], {'default': "'123'", 'max_length': '10'})
        },
        'crawler.property': {
            'Meta': {'object_name': 'Property'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'datasetLocation': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']