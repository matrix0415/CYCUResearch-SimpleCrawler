from django.db import models
from crawler.models import *

# Create your models here.
class Analyst(models.Model):
	name =models.CharField(max_length =30)
	websiteID =models.ForeignKey(Website, unique =True, limit_choices_to={'enable': True})
	nltkdataPath =models.CharField(max_length =100)
	enable =models.BooleanField(default =False, db_index =True)
	
	def __str__(self):
		return self.name


class PreprocessExportData(models.Model):	
	name =models.CharField(max_length =30)
	analystID =models.ForeignKey(Analyst)
	exportPropertyID =models.ForeignKey(ExtractionProperty)
	exceptionWords =models.CharField(max_length =150, blank =True, null =True, help_text ="words//words")
	language =models.CharField(max_length =30, default ="English")
	postagger =models.CharField(max_length =150, null =True, blank =True, help_text ="tag//tag, https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html")
	
	def __str__(self):
		return self.name	
	

class Preprocess(models.Model):
	name =models.CharField(max_length =30)
	analystID =models.ForeignKey(Analyst)
	exportDataID =models.ForeignKey(PreprocessExportData)
	propertyFilterID =models.ForeignKey(ExtractionProperty)
	propertyFilterCondition =models.CharField(max_length =30, db_index =True)
	
	def __str__(self):
		return self.name
		
		
class Datastack(models.Model):
	analystID =models.ForeignKey(Analyst)
	preprocessID =models.ForeignKey(Preprocess)
	propertyID =models.ForeignKey(Property)
	content =models.TextField()	
	contentLen =models.IntegerField(default =0)
	
	def __str__(self):
		return self.name
		
		
class Dashboard(models.Model):
	pass