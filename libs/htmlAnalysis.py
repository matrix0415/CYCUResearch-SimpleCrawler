# -*- coding: utf-8-*-
from nltk import word_tokenize
from pattern.en import parse, Sentence
from pattern.vector import Document, Model, TFIDF

from mining.models import *
from mining.libs.saveObjs import *
from mining.libs.stringFilter import *

class htmlAnalysis:	
	
	def preparingToSave(self, sourceObj, MappingObj, instanceKey, info):
		returnData ={}
		
		returnData['websiteID'] =sourceObj.websiteID_id
		
		if MappingObj.dataInputType ==0:
			returnData['webpageCollectionID'] = sourceObj.id
			
		elif MappingObj.dataInputType ==1:
			returnData['webpageCollectionID'] = sourceObj.webpageCollectionID_id
			returnData['instanceSelfID'] =sourceObj.id
			
		returnData['webScrapeMappingID'] =MappingObj.id
		returnData['instanceKey'] =instanceKey
		returnData['content'] =info
		
		return returnData
							
							
	def infoExtractAndDataStandardize(self, info, swoListString, dataOutputMean, scrapeHTMLObj):
		dataContent =""
		dataContentReadyToSave =""
		
		if dataOutputMean ==0:	# HTML
			dataContentReadyToSave =str(info)
			
		else:	
			if not scrapeHTMLObj.getDataFromHTMLAttribute:		
				dataContent =info.get_text()
			else:											# get data from attribute
				dataContent =info[scrapeHTMLObj.attributeName]
				
				if type(dataContent) ==list:
					dataContent =" ".join(dataContent)
			
			if scrapeHTMLObj.splitData:
				splitDataFormate =scrapeHTMLObj.splitDataFormate.split("|||")
				dataContent =dataContent.split(splitDataFormate[0])
				splitRange =splitDataFormate[1].split('-')
				
				if len(splitRange)>1:
					if len(dataContent)==int(splitDataFormate[2]):
						tmpString =""
						for i in range(int(splitRange[0]-1), int(splitRange[1])):
							tmpString +=dataContent[i]+" "
						dataContent =tmpString
					else:
						dataContent =""
				else:
					dataContent =dataContent[int(splitDataFormate[1])]
				
			if scrapeHTMLObj.refuseData !="":
				if scrapeHTMLObj.refuseData != dataContent:
					dataContent =dataContent
				else:		
					dataContent =""	
						
			if dataOutputMean ==1 or dataOutputMean ==3:	# Comment(String) & Attribute(String)
				if scrapeHTMLObj.cleanWords:
					stFilter =stringFilter()
					dataContentReadyToSave =stFilter.wordCleaner(swoListString, dataContent)
				else:
					dataContentReadyToSave =dataContent
				
			elif dataOutputMean ==2:	# Rating (Integer)
				dataContentReadyToSave =float(dataContent)
		
		return dataContentReadyToSave
		
	
	def scrapingDataFromHTML(self, html, scrapeHTMLObj):		
		from mining.libs.htmlTools import htmlTools
		htmlTools =htmlTools()
		fetchRs =htmlTools.soupSelector(html, scrapeHTMLObj.soupSelector)
		
		return fetchRs
	
		
	def fetchHTMLSourceFromDatabase(self, fetchObjList):		#fetchObj=[dataInputType, id]
		source =""
		sourceDic ={}
		
		if fetchObjList[0] ==0:	# From WebpageCollection
			source =webpageCollection.objects.get(id =fetchObjList[1])
			sourceDic ={"obj": source, "html": source.html}
			
		elif fetchObjList[0] ==1:	# From Instance
			source =instance.objects.get(id =fetchObjList[1])
			sourceDic ={"obj": source, "html": source.content}
			
		return sourceDic
		
	
	def htmlAnalysisMain(self, MappingObj):
		'''
		get HTML Sources
		extract Data
		normalization Data
		save Data
		'''
		if MappingObj.dataInputType ==0:		# HTML, Source from webpageCollection
			excludeIDList =list(instance.objects
				.values_list('webpageCollectionID', flat =True)
				.distinct()
				.filter(webScrapeMappingID =MappingObj.id)
				.order_by('webpageCollectionID')
			)
			
			IDList =webpageCollection.objects.exclude(
				id__in =excludeIDList
			).filter(
				websiteID =MappingObj.websiteID, 
				enable =True, 
				used =False, 
				page404 =False
			).order_by('id')
			
		elif MappingObj.dataInputType ==1:		# HTML, Source from Instance
			excludeIDList =list(instance.objects
				.values_list('instanceSelfID', flat =True)
				.distinct()
				.filter(webScrapeMappingID =MappingObj.id)
				.order_by('webpageCollectionID')
			)
			
			IDList =instance.objects.exclude(
				id__in =excludeIDList
			).filter(
				websiteID =MappingObj.websiteID, 
				webScrapeMappingID__dataOutputMean =0,
				used =False
			).order_by('id')
				
		sObj =saveObj("instance")
		swoList =stopWord.objects.values('word').get(websiteID =MappingObj.websiteID_id)
		
		for ObjID in list(IDList.values_list('id', flat =True)):
			dataList =[]
			readyData ={}
			sourceObjDic ={}
			instanceKey =-1
			
			sourceObjDic =self.fetchHTMLSourceFromDatabase([MappingObj.dataInputType, ObjID])
			dataList =self.scrapingDataFromHTML(sourceObjDic['html'], MappingObj.scrapeHTML)
			
			for data in dataList:
				info =""
				
				info =self.infoExtractAndDataStandardize(
					data, swoList['word'], MappingObj.dataOutputMean, MappingObj.scrapeHTML
				)
				
				if MappingObj.dataInputType ==1:
					instanceKey =sourceObjDic['obj'].instanceKey
				else:
					instanceKey+=1
				
				readyData =self.preparingToSave(sourceObjDic['obj'], MappingObj, instanceKey, info)
				print readyData
				print sObj.saveForm(readyData)		
				print
								
		return True
					