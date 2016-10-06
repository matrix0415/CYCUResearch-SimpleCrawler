# -*- coding: utf-8-*-
from bs4 import BeautifulSoup

from mining.libs.saveObjs import *
from mining.libs.stringFilter import *

class scrapyTools:
	def __init__(self, id):
		self.websiteID =id
		
	def setScrappingInfo(self, collectionID, html):
		self.webpageCollectionID =collectionID
		self.soup =BeautifulSoup(html, from_encoding ="UTF-8")
		
	# dictionary =[ScrapeHTML.values(), ] per website
	def scrapping(self, dic, scrapeid):
		rslist =[]
		dict ={}
		tempList =[]
		saveRs =[False,""]
		elementCount =0
		scrapeID =1
		if scrapeid !="":
			scrapeID =scrapeid
		errorCount =1
		
		
		for k in self.soup.select(dic['soupSelector']):
			dict['scrapeHTMLID'] =dic['id']
			dict['websiteID'] =self.websiteID
			dict['webpageCollectionID'] =self.webpageCollectionID
			dict['instanceKey'] =scrapeID		
		
			if not dic['getDataFromAttribute']:
				if dic['dataType'] =="html":
					content =k
				elif dic['dataType'] =="string":
					content =k.get_text()
					content =wordCleaner(self.websiteID, content)
				else:
					content =k.get_text()
			else:
				content =k[dic['attributeName']]
				
			if dic['splitData']:
				splitDataFormate =dic['splitDataFormate'].split("|||")
				content =content.split(splitDataFormate[0])[int(splitDataFormate[1])]
			
			if dic['refuseData'] != content:
				dict['content'] =content
			else:		
				dict['content'] =""
				
			so =saveObj("instance")
			saveRs =so.saveForm(dict)
			scrapeID +=1
			
		return saveRs
		
		