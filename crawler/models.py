from django.db import models
		
class Website(models.Model):
	name =models.CharField(max_length =30)
	datasetSource =models.CharField(max_length =10)
	canExtract =models.BooleanField(default =False)
	enable =models.BooleanField(default =False)
	checkDataset =models.BooleanField(default =False)
	datasetLocation =models.CharField(max_length =150, blank =True, null =True)
	datasetFileNum =models.IntegerField(default =0)
	Extracted =models.BooleanField(default =False)
	
	def __str__(self):
		return self.name

		
class CrawlProperty(models.Model):
	websiteID =models.ForeignKey(Website)
	url =models.URLField()
	page404Path =models.URLField()
	nJobs =models.IntegerField(default =1)
	
	class Meta:
		ordering =['websiteID', 'url']
		unique_together =("websiteID", "url")
		
	def __str__(self):
		return self.url
	
	
class ExtractionEntity(models.Model):
	name =models.CharField(max_length =30)
	websiteID =models.ForeignKey(Website)
	entitySelector =models.CharField(max_length =100, db_index =True)
	
	class Meta:
		ordering =['websiteID', 'entitySelector']
		unique_together =("websiteID", "entitySelector")
		
	def __str__(self):
		return self.name
	
	
class ExtractionProperty(models.Model):
	name =models.CharField(max_length =30)
	extractionEntityID =models.ForeignKey(ExtractionEntity)
	propertySelector =models.CharField(max_length =100)
	
	class Meta:
		ordering =['extractionEntityID', 'propertySelector']
		unique_together =('extractionEntityID', 'propertySelector')
		
	def __str__(self):
		return self.name

		
class Entity(models.Model):
	websiteID =models.ForeignKey(Website)
	extractionEntityID =models.ForeignKey(ExtractionEntity)
	datasetPath =models.CharField(max_length =150)
	content =models.TextField(blank =True, null =True)
	used =models.BooleanField(default =False, db_index =True)
	datetime =models.DateTimeField(auto_now_add =True)
	
	def __str__(self):
		return str(self.id)
		
	
class Property(models.Model):
	entityID =models.ForeignKey(Entity, db_index =True)
	extractionPropertyID =models.ForeignKey(ExtractionProperty)
	content =models.TextField(blank =True, null =True, db_index =True)
	datetime =models.DateTimeField(auto_now_add =True)
	
	def __str__(self):
		return self.extractionPropertyID.name
