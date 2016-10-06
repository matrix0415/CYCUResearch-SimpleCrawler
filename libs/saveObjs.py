# -*- coding: utf-8-*-
from mining.forms import *
from mining.models import *


class saveObj:
	def __init__(self, modelName):
		self.modelName =modelName
	
	def setModelName(self, modelName):
		self.modelName =modelName
	
	def saveForm(self, datadic):
		try:
			rs =[True, ""]
			
			if self.modelName =="instance":
				inceForm =instanceForm(datadic)
				
			elif self.modelName =="opinionAttributeAssembling":
				inceForm =opinionAttributeAssemblingForm(datadic)
				
			elif self.modelName =="opinionAttributeMapping":
				inceForm =opinionAttributeMappingForm(datadic)
				
			elif self.modelName =="opinionFlattening":
				inceForm =opinionFlatteningForm(datadic)
				
			elif self.modelName =="webpageCollection":
				inceForm =webpageCollectionForm(datadic)
				
			elif self.modelName =="scrapeHTML":
				inceForm =scrapeHTMLForm(datadic)
				
			elif self.modelName =="website":
				inceForm =websiteForm(datadic)
				
			elif self.modelName =="stopWord":
				inceForm =stopWordForm(datadic)
				
			if inceForm.is_valid():
				inceForm.save()
				del(datadic)
				del(inceForm)
				
			else:
				rs[0] =False
				rs[1] =inceForm.errors
				
		except Exception as e:
			rs[0] =False
			rs[1] =str(e)
			
		return rs
	
	def saveMultiRows(self, datadicList):	
		
		for datadic in datadicList:
			print(self.saveForm(datadic))
			
			