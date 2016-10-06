# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Entity.datetime'
        db.delete_column('crawler_entity', 'datetime')

        # Deleting field 'Entity.entityPath'
        db.delete_column('crawler_entity', 'entityPath')

        # Deleting field 'Entity.datasetPath'
        db.delete_column('crawler_entity', 'datasetPath')

        # Deleting field 'Entity.used'
        db.delete_column('crawler_entity', 'used')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Entity.datetime'
        raise RuntimeError("Cannot reverse this migration. 'Entity.datetime' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Entity.datetime'
        db.add_column('crawler_entity', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Entity.entityPath'
        raise RuntimeError("Cannot reverse this migration. 'Entity.entityPath' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Entity.entityPath'
        db.add_column('crawler_entity', 'entityPath',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Entity.datasetPath'
        raise RuntimeError("Cannot reverse this migration. 'Entity.datasetPath' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Entity.datasetPath'
        db.add_column('crawler_entity', 'datasetPath',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)

        # Adding field 'Entity.used'
        db.add_column('crawler_entity', 'used',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


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
            'Meta': {'object_name': 'Entity', 'ordering': "['websiteID', 'entitySelector']", 'unique_together': "(('websiteID', 'entitySelector'),)"},
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
            'splitDataFormate': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
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
            'datasetFileNum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'datasetLocation': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '150', 'null': 'True'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']