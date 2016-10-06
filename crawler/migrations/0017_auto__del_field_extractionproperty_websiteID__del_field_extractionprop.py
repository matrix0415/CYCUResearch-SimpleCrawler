# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Property', fields ['extractionPropertyID', 'entityID']
        db.delete_unique('crawler_property', ['extractionPropertyID_id', 'entityID_id'])

        # Deleting field 'ExtractionProperty.websiteID'
        db.delete_column('crawler_extractionproperty', 'websiteID_id')

        # Deleting field 'ExtractionProperty.getFromAttribute'
        db.delete_column('crawler_extractionproperty', 'getFromAttribute')

        # Deleting field 'ExtractionProperty.instanceSelector'
        db.delete_column('crawler_extractionproperty', 'instanceSelector')

        # Deleting field 'ExtractionProperty.entitySelector'
        db.delete_column('crawler_extractionproperty', 'entitySelector')

        # Deleting field 'ExtractionProperty.splitDataFormate'
        db.delete_column('crawler_extractionproperty', 'splitDataFormate')

        # Adding field 'ExtractionProperty.extractionEntityID'
        db.add_column('crawler_extractionproperty', 'extractionEntityID',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionEntity'], default=datetime.datetime(2014, 7, 9, 0, 0)),
                      keep_default=False)

        # Adding field 'ExtractionProperty.propertySelector'
        db.add_column('crawler_extractionproperty', 'propertySelector',
                      self.gf('django.db.models.fields.CharField')(default='123', max_length=100),
                      keep_default=False)

        # Adding unique constraint on 'ExtractionProperty', fields ['extractionEntityID', 'propertySelector']
        db.create_unique('crawler_extractionproperty', ['extractionEntityID_id', 'propertySelector'])

        # Deleting field 'Property.entityID'
        db.delete_column('crawler_property', 'entityID_id')


    def backwards(self, orm):
        # Removing unique constraint on 'ExtractionProperty', fields ['extractionEntityID', 'propertySelector']
        db.delete_unique('crawler_extractionproperty', ['extractionEntityID_id', 'propertySelector'])


        # User chose to not deal with backwards NULL issues for 'ExtractionProperty.websiteID'
        raise RuntimeError("Cannot reverse this migration. 'ExtractionProperty.websiteID' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ExtractionProperty.websiteID'
        db.add_column('crawler_extractionproperty', 'websiteID',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website']),
                      keep_default=False)

        # Adding field 'ExtractionProperty.getFromAttribute'
        db.add_column('crawler_extractionproperty', 'getFromAttribute',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ExtractionProperty.instanceSelector'
        raise RuntimeError("Cannot reverse this migration. 'ExtractionProperty.instanceSelector' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ExtractionProperty.instanceSelector'
        db.add_column('crawler_extractionproperty', 'instanceSelector',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ExtractionProperty.entitySelector'
        raise RuntimeError("Cannot reverse this migration. 'ExtractionProperty.entitySelector' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ExtractionProperty.entitySelector'
        db.add_column('crawler_extractionproperty', 'entitySelector',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100),
                      keep_default=False)

        # Adding field 'ExtractionProperty.splitDataFormate'
        db.add_column('crawler_extractionproperty', 'splitDataFormate',
                      self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=30),
                      keep_default=False)

        # Deleting field 'ExtractionProperty.extractionEntityID'
        db.delete_column('crawler_extractionproperty', 'extractionEntityID_id')

        # Deleting field 'ExtractionProperty.propertySelector'
        db.delete_column('crawler_extractionproperty', 'propertySelector')


        # User chose to not deal with backwards NULL issues for 'Property.entityID'
        raise RuntimeError("Cannot reverse this migration. 'Property.entityID' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Property.entityID'
        db.add_column('crawler_property', 'entityID',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionEntity']),
                      keep_default=False)

        # Adding unique constraint on 'Property', fields ['extractionPropertyID', 'entityID']
        db.create_unique('crawler_property', ['extractionPropertyID_id', 'entityID_id'])


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
            'Meta': {'unique_together': "(('websiteID', 'entitySelector'),)", 'object_name': 'ExtractionEntity', 'ordering': "['websiteID', 'entitySelector']"},
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'InstanceCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'unique_together': "(('extractionEntityID', 'propertySelector'),)", 'object_name': 'ExtractionProperty', 'ordering': "['extractionEntityID', 'propertySelector']"},
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
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
            'datasetLocation': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True', 'null': 'True'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']