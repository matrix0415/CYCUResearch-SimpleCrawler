# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Analyst', fields ['enable']
        db.create_index('analyzer_analyst', ['enable'])


    def backwards(self, orm):
        # Removing index on 'Analyst', fields ['enable']
        db.delete_index('analyzer_analyst', ['enable'])


    models = {
        'analyzer.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nltkdataPath': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']", 'unique': 'True'})
        },
        'analyzer.dashboard': {
            'Meta': {'object_name': 'Dashboard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'analyzer.datastack': {
            'Meta': {'object_name': 'Datastack'},
            'analystID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.Analyst']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'contentLen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preprocessID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.Preprocess']"}),
            'propertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Property']"})
        },
        'analyzer.preprocess': {
            'Meta': {'object_name': 'Preprocess'},
            'analystID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.Analyst']"}),
            'exceptionWords': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'}),
            'exportPropertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"}),
            'exportPropertyRegex': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'English'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postagger': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'analyzer.preprocesscondition': {
            'Meta': {'object_name': 'PreprocessCondition'},
            'preprocessID': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['analyzer.Preprocess']", 'unique': 'True', 'primary_key': 'True'}),
            'propertyFilterCondition': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'propertyFilterID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"})
        },
        'crawler.entity': {
            'Meta': {'object_name': 'Entity'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'datasetPath': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionentity': {
            'Meta': {'unique_together': "(('websiteID', 'entitySelector'),)", 'object_name': 'ExtractionEntity', 'ordering': "['websiteID', 'entitySelector']"},
            'entitySelector': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
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
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'db_index': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'datasetLocation': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['analyzer']