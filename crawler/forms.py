from django.forms import ModelForm
'''
from crawler.models import *

class WebsiteForm(ModelForm):
	class Meta:
		model =Website

class CrawlPropertyForm(ModelForm):
	class Meta:
		model =CrawlProperty
		
class ExtractionPropertyForm(ModelForm):
	class Meta:
		model =ExtractionProperty

class EntityForm(ModelForm):
	class Meta:
		model =Entity

class InstanceForm(ModelForm):
	class Meta:
		model =Instance
		
'''
		
'''
from django import forms
class webScrapeMappingForm(ModelForm):
	dataType =forms.TypedChoiceField(widget=forms.RadioSelect, coerce =int)
	sequence =forms.TypedChoiceField(coerce =int)
	
	class Meta:
		model =webScrapeMapping
'''				