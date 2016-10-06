# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ExtractionEntity', fields ['websiteID', 'entitySelector']
        db.delete_unique('crawler_extractionentity', ['websiteID_id', 'entitySelector'])

        # Deleting model 'ExtractionEntity'
        db.delete_table('crawler_extractionentity')

        # Adding model 'Entity'
        db.create_table('crawler_entity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('entitySelector', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('crawler', ['Entity'])

        # Adding unique constraint on 'Entity', fields ['websiteID', 'entitySelector']
        db.create_unique('crawler_entity', ['websiteID_id', 'entitySelector'])


        # Changing field 'Instance.entityID'
        db.alter_column('crawler_instance', 'entityID_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Entity']))

    def backwards(self, orm):
        # Removing unique constraint on 'Entity', fields ['websiteID', 'entitySelector']
        db.delete_unique('crawler_entity', ['websiteID_id', 'entitySelector'])

        # Adding model 'ExtractionEntity'
        db.create_table('crawler_extractionentity', (
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entitySelector', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('crawler', ['ExtractionEntity'])

        # Adding unique constraint on 'ExtractionEntity', fields ['websiteID', 'entitySelector']
        db.create_unique('crawler_extractionentity', ['websiteID_id', 'entitySelector'])

        # Deleting model 'Entity'
        db.delete_table('crawler_entity')


        # Changing field 'Instance.entityID'
        db.alter_column('crawler_instance', 'entityID_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionEntity']))

    models = {
        'crawler.crawlproperty': {
            'Meta': {'ordering': "['websiteID', 'url']", 'unique_together': "(('websiteID', 'url'),)", 'object_name': 'CrawlProperty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nJobs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'page404Path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.entity': {
            'Meta': {'ordering': "['websiteID', 'entitySelector']", 'unique_together': "(('websiteID', 'entitySelector'),)", 'object_name': 'Entity'},
            'entitySelector': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'splitDataFormate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.instance': {
            'Meta': {'ordering': "['extractionPropertyID', 'entityID']", 'unique_together': "(('extractionPropertyID', 'entityID'),)", 'object_name': 'Instance'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'datasetLocation': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']