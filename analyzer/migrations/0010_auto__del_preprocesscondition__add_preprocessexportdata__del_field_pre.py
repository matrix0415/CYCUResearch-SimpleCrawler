# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PreprocessCondition'
        db.delete_table('analyzer_preprocesscondition')

        # Adding model 'PreprocessExportData'
        db.create_table('analyzer_preprocessexportdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('exportPropertyID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('exceptionWords', self.gf('django.db.models.fields.CharField')(null=True, max_length=150, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='English', max_length=30)),
            ('postagger', self.gf('django.db.models.fields.CharField')(null=True, max_length=150, blank=True)),
        ))
        db.send_create_signal('analyzer', ['PreprocessExportData'])

        # Deleting field 'Preprocess.exportPropertyID'
        db.delete_column('analyzer_preprocess', 'exportPropertyID_id')

        # Deleting field 'Preprocess.postagger'
        db.delete_column('analyzer_preprocess', 'postagger')

        # Deleting field 'Preprocess.language'
        db.delete_column('analyzer_preprocess', 'language')

        # Deleting field 'Preprocess.exceptionWords'
        db.delete_column('analyzer_preprocess', 'exceptionWords')

        # Adding field 'Preprocess.exportDataID'
        db.add_column('analyzer_preprocess', 'exportDataID',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['analyzer.PreprocessExportData']),
                      keep_default=False)

        # Adding field 'Preprocess.propertyFilterID'
        db.add_column('analyzer_preprocess', 'propertyFilterID',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['crawler.ExtractionProperty']),
                      keep_default=False)

        # Adding field 'Preprocess.propertyFilterCondition'
        db.add_column('analyzer_preprocess', 'propertyFilterCondition',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default=1, max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PreprocessCondition'
        db.create_table('analyzer_preprocesscondition', (
            ('propertyFilterCondition', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=30)),
            ('propertyFilterID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('preprocessID', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['analyzer.Preprocess'])),
        ))
        db.send_create_signal('analyzer', ['PreprocessCondition'])

        # Deleting model 'PreprocessExportData'
        db.delete_table('analyzer_preprocessexportdata')


        # User chose to not deal with backwards NULL issues for 'Preprocess.exportPropertyID'
        raise RuntimeError("Cannot reverse this migration. 'Preprocess.exportPropertyID' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Preprocess.exportPropertyID'
        db.add_column('analyzer_preprocess', 'exportPropertyID',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty']),
                      keep_default=False)

        # Adding field 'Preprocess.postagger'
        db.add_column('analyzer_preprocess', 'postagger',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=150, blank=True),
                      keep_default=False)

        # Adding field 'Preprocess.language'
        db.add_column('analyzer_preprocess', 'language',
                      self.gf('django.db.models.fields.CharField')(default='English', max_length=30),
                      keep_default=False)

        # Adding field 'Preprocess.exceptionWords'
        db.add_column('analyzer_preprocess', 'exceptionWords',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=150, blank=True),
                      keep_default=False)

        # Deleting field 'Preprocess.exportDataID'
        db.delete_column('analyzer_preprocess', 'exportDataID_id')

        # Deleting field 'Preprocess.propertyFilterID'
        db.delete_column('analyzer_preprocess', 'propertyFilterID_id')

        # Deleting field 'Preprocess.propertyFilterCondition'
        db.delete_column('analyzer_preprocess', 'propertyFilterCondition')


    models = {
        'analyzer.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nltkdataPath': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['crawler.Website']"})
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
            'exportDataID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analyzer.PreprocessExportData']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'propertyFilterCondition': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30'}),
            'propertyFilterID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"})
        },
        'analyzer.preprocessexportdata': {
            'Meta': {'object_name': 'PreprocessExportData'},
            'exceptionWords': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'}),
            'exportPropertyID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionProperty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'English'", 'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postagger': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'})
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
            'Meta': {'object_name': 'ExtractionEntity', 'unique_together': "(('websiteID', 'entitySelector'),)", 'ordering': "['websiteID', 'entitySelector']"},
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'Meta': {'object_name': 'ExtractionProperty', 'unique_together': "(('extractionEntityID', 'propertySelector'),)", 'ordering': "['extractionEntityID', 'propertySelector']"},
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'propertySelector': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crawler.property': {
            'Meta': {'object_name': 'Property'},
            'content': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
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