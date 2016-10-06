# -*- coding: utf-8-*-
import mechanize, gzip
from bs4 import BeautifulSoup

class htmlTools:
	# Compress the html file, you won't use it directly when you need to get the html file.
	def ungzipResponse(self, r,b):
		headers = r.info()
		if headers['Content-Encoding']=='gzip':
			gz = gzip.GzipFile(fileobj=r, mode='rb')
			html = gz.read()
			gz.close()
			headers["Content-type"] = "text/html; charset=utf-8"
			r.set_data( html )
			b.set_response(r)
			return html

	# Open the URL to get the html file.	
	def openUrl(self, url, page404):
		html =""
		br =mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders.append(['Accept-Encoding','gzip'])
		br.addheaders.append(['Accept-Language', 'en-US;q=0.6,en;q=0.4'])
		try:
			response =br.open(url)
			htmlsource =self.ungzipResponse(response, br)
			if br.geturl() ==page404:
				html =[False, '404']
			elif '404' in html:
				html =[False, '404']	
			else:
				html =[True, htmlsource]
		except Exception as e:
			html =[False, e]
		return html
	
	# Put html/xml and selector in side and it will filter the element you want inside the html/xml file.
	def soupSelector(self, html, cssSelector):
		bSoup =BeautifulSoup(html, from_encoding ="UTF-8")
		return bSoup.select(cssSelector)
	
	
	def setWebsiteCURLList(self, websiteCURLList):
		self.websiteCURLList =websiteCURLList
		
		
	def collectionWebpage(self, websiteInfo, id, page):
		rs =False
		
		print(websiteInfo['name'])
		print('Instance:', id)
		count =len(websiteInfo['urlParameter'].split('|'))
		if count>1:
			url =websiteInfo['url']%(id, page)
			print('page:', page)				
		elif count>0:
			url =websiteInfo['url']%(id)	
		else:
			url =websiteInfo['url']
			
		try:
			self.websiteCURLList.remove(url)
			print("URL is Exist.")
			print(len(self.websiteCURLList))
		except ValueError:
			html =self.openUrl(url, websiteInfo['page404'])
			
			collection ={}
			collection['websiteID'] =websiteInfo['id']
			collection['url'] =url		
			
			if html[0]:
				collection['page404'] =False
				soupRs =self.soupSelector(html[1], websiteInfo['mustExistSoupSelector'])
				if len(soupRs)>0:
					print("Element Existing, HTML available.")
					if websiteInfo['getHtmlSoupSelector'] !='':
						tmp =self.soupSelector(html[1], websiteInfo['getHtmlSoupSelector'])
						if len(tmp) is 1:
							tmpHtml =tmp[0]
						else:
							tmpHtml =" ".join(tmp)
					else:
						tmpHtml =html[1]
						
					collection['enable'] =True
					collection['html'] =tmpHtml#sf.removeRedundentSpace(tmpHtml)
					rs =True
				else:
					collection['page404'] =True
					collection['enable'] =False
				
				from mining.libs.saveObjs import *
				
				so =saveObj("webpageCollection")
				fo =so.saveForm(collection)
				print(fo)
				
		return rs
		
		
'''
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
					swo =stopWord.objects.values('word').get(websiteID =websiteID)
					content =wordCleaner(swo['word'], content)
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
		
'''