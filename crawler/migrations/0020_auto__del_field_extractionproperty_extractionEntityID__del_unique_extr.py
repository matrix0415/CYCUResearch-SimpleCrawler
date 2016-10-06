# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ExtractionProperty', fields ['extractionEntityID', 'propertySelector']
        db.delete_unique('crawler_extractionproperty', ['extractionEntityID_id', 'propertySelector'])

        # Deleting field 'ExtractionProperty.extractionEntityID'
        db.delete_column('crawler_extractionproperty', 'extractionEntityID_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ExtractionProperty.extractionEntityID'
        raise RuntimeError("Cannot reverse this migration. 'ExtractionProperty.extractionEntityID' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ExtractionProperty.extractionEntityID'
        db.add_column('crawler_extractionproperty', 'extractionEntityID',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionEntity']),
                      keep_default=False)

        # Adding unique constraint on 'ExtractionProperty', fields ['extractionEntityID', 'propertySelector']
        db.create_unique('crawler_extractionproperty', ['extractionEntityID_id', 'propertySelector'])


    models = {
        'crawler.crawlproperty': {
            'Meta': {'unique_together': "(('websiteID', 'url'),)", 'ordering': "['websiteID', 'url']", 'object_name': 'CrawlProperty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nJobs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'page404Path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionentity': {
            'EntityCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'unique_together': "(('websiteID', 'entitySelector'),)", 'ordering': "['websiteID', 'entitySelector']", 'object_name': 'ExtractionEntity'},
            'entityPath': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'Meta': {'object_name': 'ExtractionProperty'},
            'PropertyCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'propertySelector': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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