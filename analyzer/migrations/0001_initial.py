# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Analyst'
        db.create_table('analyzer_analyst', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
        ))
        db.send_create_signal('analyzer', ['Analyst'])

        # Adding model 'Preprocess'
        db.create_table('analyzer_preprocess', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('analystID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analyzer.Analyst'])),
            ('exportPropertyID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('exportPropertyRegex', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100)),
            ('language', self.gf('django.db.models.fields.CharField')(default='English', max_length=30)),
            ('postagger', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nltkdataPath', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('analyzer', ['Preprocess'])

        # Adding model 'PreprocessCondition'
        db.create_table('analyzer_preprocesscondition', (
            ('preprocessID', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['analyzer.Preprocess'])),
            ('propertyFilterID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('propertyFilterCondition', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=30)),
        ))
        db.send_create_signal('analyzer', ['PreprocessCondition'])

        # Adding model 'Datastack'
        db.create_table('analyzer_datastack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('analystID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analyzer.Analyst'])),
            ('preprocessID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analyzer.Preprocess'])),
            ('propertyID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Property'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('analyzer', ['Datastack'])

        # Adding model 'Dashboard'
        db.create_table('analyzer_dashboard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('analyzer', ['Dashboard'])


    def backwards(self, orm):
        # Deleting model 'Analyst'
        db.delete_table('analyzer_analyst')

        # Deleting model 'Preprocess'
        db.delete_table('analyzer_preprocess')

        # Deleting model 'PreprocessCondition'
        db.delete_table('analyzer_preprocesscondition')

        # Deleting model 'Datastack'
        db.delete_table('analyzer_datastack')

        # Deleting model 'Dashboard'
        db.delete_table('analyzer_dashboard')


    models = {
        'analyzer.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
            'language': ('django.db.models.fields.CharField', [], {'default': "'English'", 'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nltkdataPath': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postagger': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'analyzer.preprocesscondition': {
            'Meta': {'object_name': 'PreprocessCondition'},
            'preprocessID': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'primary_key': 'True', 'to': "orm['analyzer.Preprocess']"}),
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
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionentity': {
            'Meta': {'ordering': "['websiteID', 'entitySelector']", 'unique_together': "(('websiteID', 'entitySelector'),)", 'object_name': 'ExtractionEntity'},
            'entitySelector': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.extractionproperty': {
            'Meta': {'ordering': "['extractionEntityID', 'propertySelector']", 'unique_together': "(('extractionEntityID', 'propertySelector'),)", 'object_name': 'ExtractionProperty'},
            'extractionEntityID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.ExtractionEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'propertySelector': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crawler.property': {
            'Meta': {'object_name': 'Property'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
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
            'datasetLocation': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '150'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['analyzer']