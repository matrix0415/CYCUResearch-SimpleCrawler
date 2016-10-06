# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Analyst.nltkdataPath'
        db.add_column('analyzer_analyst', 'nltkdataPath',
                      self.gf('django.db.models.fields.CharField')(max_length=100, default='/home/matrix/textminng/nltk_data/'),
                      keep_default=False)

        # Deleting field 'Preprocess.nltkdataPath'
        db.delete_column('analyzer_preprocess', 'nltkdataPath')


    def backwards(self, orm):
        # Deleting field 'Analyst.nltkdataPath'
        db.delete_column('analyzer_analyst', 'nltkdataPath')


        # User chose to not deal with backwards NULL issues for 'Preprocess.nltkdataPath'
        raise RuntimeError("Cannot reverse this migration. 'Preprocess.nltkdataPath' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Preprocess.nltkdataPath'
        db.add_column('analyzer_preprocess', 'nltkdataPath',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


    models = {
        'analyzer.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nltkdataPath': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'analyzer.dashboard': {
            'Meta': {'object_name': 'Dashboard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'analyzer.datastack': {
            'Meta': {'object_name': 'Datastack'},
            'analystID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.Analyst']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preprocessID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.Preprocess']"}),
            'propertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Property']"})
        },
        'analyzer.preprocess': {
            'Meta': {'object_name': 'Preprocess'},
            'analystID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.Analyst']"}),
            'exportPropertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"}),
            'exportPropertyRegex': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'English'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postagger': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'analyzer.preprocesscondition': {
            'Meta': {'object_name': 'PreprocessCondition'},
            'preprocessID': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['analyzer.Preprocess']", 'unique': 'True'}),
            'propertyFilterCondition': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30'}),
            'propertyFilterID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"})
        },
        'crawler.entity': {
            'Meta': {'object_name': 'Entity'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'datasetPath': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionentity': {
            'Meta': {'unique_together': "(('websiteID', 'entitySelector'),)", 'object_name': 'ExtractionEntity', 'ordering': "['websiteID', 'entitySelector']"},
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'Meta': {'unique_together': "(('extractionEntityID', 'propertySelector'),)", 'object_name': 'ExtractionProperty', 'ordering': "['extractionEntityID', 'propertySelector']"},
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'propertySelector': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crawler.property': {
            'Meta': {'object_name': 'Property'},
            'content': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'entityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Entity']"}),
            'extractionPropertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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

    complete_apps = ['analyzer']