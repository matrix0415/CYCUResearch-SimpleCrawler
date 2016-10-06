# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Website'
        db.create_table('crawler_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('datasetSource', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('canExtract', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('checkDataset', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Extracted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('crawler', ['Website'])

        # Adding model 'CrawlProperty'
        db.create_table('crawler_crawlproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('exportMethod', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('page404Path', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('nJobs', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('crawler', ['CrawlProperty'])

        # Adding unique constraint on 'CrawlProperty', fields ['websiteID', 'url']
        db.create_unique('crawler_crawlproperty', ['websiteID_id', 'url'])

        # Adding model 'ExtractionProperty'
        db.create_table('crawler_extractionproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('entitySelector', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('instanceSelector', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('getFromAttribute', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('splitDataFormate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('InstanceCount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('crawler', ['ExtractionProperty'])

        # Adding model 'Entity'
        db.create_table('crawler_entity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('entitySelector', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('crawler', ['Entity'])

        # Adding model 'Instance'
        db.create_table('crawler_instance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('websiteID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Website'])),
            ('extractionPropertyID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.ExtractionProperty'])),
            ('entityID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crawler.Entity'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('crawler', ['Instance'])

        # Adding unique constraint on 'Instance', fields ['extractionPropertyID', 'entityID']
        db.create_unique('crawler_instance', ['extractionPropertyID_id', 'entityID_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Instance', fields ['extractionPropertyID', 'entityID']
        db.delete_unique('crawler_instance', ['extractionPropertyID_id', 'entityID_id'])

        # Removing unique constraint on 'CrawlProperty', fields ['websiteID', 'url']
        db.delete_unique('crawler_crawlproperty', ['websiteID_id', 'url'])

        # Deleting model 'Website'
        db.delete_table('crawler_website')

        # Deleting model 'CrawlProperty'
        db.delete_table('crawler_crawlproperty')

        # Deleting model 'ExtractionProperty'
        db.delete_table('crawler_extractionproperty')

        # Deleting model 'Entity'
        db.delete_table('crawler_entity')

        # Deleting model 'Instance'
        db.delete_table('crawler_instance')


    models = {
        'crawler.crawlproperty': {
            'Meta': {'object_name': 'CrawlProperty', 'unique_together': "(('websiteID', 'url'),)", 'ordering': "['websiteID', 'url']"},
            'exportMethod': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
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
            'splitDataFormate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'websiteID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crawler.Website']"})
        },
        'crawler.instance': {
            'Meta': {'object_name': 'Instance', 'unique_together': "(('extractionPropertyID', 'entityID'),)", 'ordering': "['extractionPropertyID', 'entityID']"},
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
            'datasetSource': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crawler']