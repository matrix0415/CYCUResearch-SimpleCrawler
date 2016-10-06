from django.shortcuts import render
from django.http import HttpResponse
from crawler.models import *
# Create your views here.

def crawl(request):
	from os import listdir
	from os.path import dirname, abspath, join, exists
	from multiprocessing import Process
	from libs.multiprocessL import prepareForMultiprocessL
	from crawler.controller.datasetC import fetchPathC
	from crawler.controller.datasetC import importFromWebExportToFileC
	
	# Check dataset.
	siteDatasetPath =""
	sites =Website.objects.filter(enable =True)
	
	for site in sites:
		if site.datasetLocation is not None:
			siteDatasetPath =site.datasetLocation
		else:
			siteDatasetPath =join(abspath(dirname(dirname(__file__))), "dataset", site.name)
			site.datasetLocation =siteDatasetPath
			site.save()
		
		if not exists(siteDatasetPath) or len(listdir(siteDatasetPath)) ==0:	# dataset isn't ready
			crawlObjs =CrawlProperty.objects.filter(websiteID =site)
			
			for crawlObj in crawlObjs:		
				urlListRs =fetchPathC(crawlObj.url, "url")
				
				if urlListRs[0]:		
					n =0
					urlList =urlListRs[1]
					prepare =prepareForMultiprocessL(len(urlList), crawlObj.nJobs)
					
					for k in range(prepare["perJobRow"], prepare["rowUntil"], prepare["perJobRow"]):
						Process(
							target=importFromWebExportToFileC, 
							args=(site.name, urlList[n:k], crawlObj.page404Path)
						).start()
						n =k	
				else:
					print(urlListRs[1])
					
		site.checkDataset =False
		site.datasetFileNum =len(listdir(siteDatasetPath))
		site.save()
		
	return HttpResponse("Done")		
	
	
def extract(request, execType ="entity"):
	from libs.nlpLib import removeRedundentSpaceL, removeNewlineL
	from crawler.controller.datasetC import fetchPathC, extractFromHTMLC
	
	if execType =="entity":
		eeObjs =ExtractionEntity.objects.filter(websiteID__enable =True, websiteID__canExtract =True)
		excludeFpath =list(Entity.objects.values_list('datasetPath', flat =True).distinct())
		
		for eeObj in eeObjs:		
			datasetLocation =eeObj.websiteID.datasetLocation
			pathListRs =fetchPathC(datasetLocation, "file")
				
			if pathListRs[0]:
				for fpath in pathListRs[1]:					
					if fpath not in excludeFpath:
						websiteID =eeObj.websiteID
						entitiesContentRs =extractFromHTMLC(fpath, eeObj.entitySelector)
						
						if entitiesContentRs[0]:
							for entityContent in entitiesContentRs[1]:
								content =removeRedundentSpaceL(str(entityContent))
								entity =Entity.objects.create(
									websiteID =websiteID, 
									extractionEntityID =eeObj, 
									content =content,
									datasetPath =fpath
								)
								print("%s:%d.save()"%(fpath, entity.pk))
								
						else:
							print(entitiesContentRs[1])
							
					else:
						excludeFpath.remove(fpath)
						
			else:
				print(pathListRs[1])
							
	elif execType =="property":		
		eeObjs =ExtractionEntity.objects.filter(websiteID__enable =True, websiteID__canExtract =True)			
		epObjs =ExtractionProperty.objects.filter(extractionEntityID__in =eeObjs)
		entities =Entity.objects.filter(used =False)
		
		for entity in entities:
			entity.used =True
			entity.save()
			
			for epObj in epObjs:
				propertiesContentRs =extractFromHTMLC(str(entity.content), epObj.propertySelector)
				content =removeNewlineL(removeRedundentSpaceL(str(propertiesContentRs[1])))
				
				if propertiesContentRs[0]:
					property =Property.objects.create(
						entityID =entity,
						extractionPropertyID =epObj,
						content =content
					)
					
				else:
					print(propertiesContentRs[1])	
					
			print("entity-%d.save()"%(entity.pk))
			
	return HttpResponse("Done")					


def attributeCleaner(request):
	from django.db.models import Q
	from libs.nlpLib import removeNewlineL as newlineL
	from libs.nlpLib import removeRedundentSpaceL as spaceL
	from libs.fileL import fileWrite as fw
	rs =""
	trip ="else"
	rms =["genuine hotels.com guest review", "read more"]
	extract =[10, 11, 12, 13, 14, 15]
	score =["1.0", "2.0", "3.0", "4.0", "5.0"]
	attribute =["business", "family", "friends", "romance", "else"]
	
	for a in attribute:
		aEntityID =Property.objects.values_list(
			'entityID', flat =True
		).filter(
			extractionPropertyID =9, content =a
		).distinct()
		print(a)
		
		for s in score:
			for e in extract:
				sEntityID =Property.objects.values_list('entityID', flat =True).filter(
					entityID__in =aEntityID, extractionPropertyID =e, content =s
				)
				sCount =len(sEntityID)
				print("%d, %s, %d"%(e, s, sCount))
				contentList =list(
					Property.objects.values_list('content', flat =True).filter(
						Q(entityID__in =sEntityID), (
							Q(extractionPropertyID =16) | 
							Q(extractionPropertyID =17)
						)
					)
				)
				contentList =[
					newlineL(
						spaceL(
							i.lower().replace(rms[0], "").replace(rms[1], "")
						)
					) for i in contentList
				
				]
				content ="\n".join(contentList)
				fwrs =fw("/home/ubuntu/textmining/textmining_v2/dataset/Hotels.com/%s_%s_%d"%(a, s, e), content)
				print(fwrs)
				rs +="%s : %s : %d : %d : %s<br/>"%(a, s, e, sCount, str(""))
			rs+="<br/><br/>"
		rs+="<br/><br/><br/>"
	
	'''
	attriPropList =Property.objects.values_list(
		'content', flat =True
	).filter(
		extractionPropertyID =9
	).order_by(
		'content'
	).distinct()
	
	for attriProp in list(attriPropList):
		attriPropList =Property.objects.values_list(
			'entityID', flat =True
		).filter(
			extractionPropertyID =9, content =attriProp
		).distinct()
		print(1)
		for i in ["1.0", "2.0", "3.0", "4.0", "5.0"]:
			attriPropListI =Property.objects.values_list('entityID', flat =True).filter(
				entityID__in =attriPropList, content =i
			)
			print(2)
			for j in range(10, 16):
				attriPropListJ =Property.objects.values_list('entityID').filter(
					entityID__in =attriPropListI, extractionPropertyID =j
				).count()
				print(3)
				rs +="%s : %s : %d : %d<br/>"%(attriProp, i, j, attriPropListJ)
			rs +="<br/><br/>"
		rs +="<br/><br/><br/>"
	rs +="<br/><br/><br/><br/>"
	'''
	'''
	oriattri =attriProp
	attriProp =removePunctuationL(removeNewlineL(removeRedundentSpaceL(str(attriProp))))
	attrSplit =attriProp.split(" ")
	attrLen =len(attrSplit)
	if attrLen>1:
		if attrSplit[1] =="trip":
			if attrLen>4:
				trip =attrSplit[3]
			else:
				trip ="else"
		else:
			trip =attrSplit[1]
	else:
		trip ="else"		
	#p =Property.objects.filter(extractionPropertyID =9, content =oriattri).update(content =trip)
	#  
	'''
	#rs +="%d : %s : %s, %s, %s<br/>"%(attrLen, trip, attriProp, str(attrSplit), oriattri)
		
	return HttpResponse(rs)	
	

def test(request):
	
	n =0
	k =0
	tw =0
	tr =0
	scores =["1.0", "2.0", "3.0", "4.0", "5.0"]
	rates =[10, 11, 12, 13, 14, 15]
	rs ="Total not used Entity : "+str(Entity.objects.filter(used =False).count())+"<hr/>"
	
	for rate in rates:
		rateAggregate =Property.objects.exclude(content ="").filter(extractionPropertyID =rate).count()
		
		for score in scores:
			poclist =Property.objects.values_list(
				'entityID', flat =True
			).exclude(
				content =""
			).filter(
				extractionPropertyID =rate, content =score
			).distinct()
			'''
			reviews =" ".join(
				Property.objects.values_list(
					'content', flat =True
				).filter(
					extractionPropertyID =16, entityID__in =poclist
				)
			)
			'''
			tentity =len(poclist)
			#twords =len(reviews.split(" "))
			#tw +=twords
			tr +=tentity
			rs +=str(rate)+"<br/>"
			rs +="Equal to Score : %s<br/>"%score
			rs +="Total Opinion : %d => %s<br/>"%(tentity, str(tentity/rateAggregate))
			#rs +="Total Opinion Words : %d<br/>"%twords
			#rs +="Words Per Opinion : %s<br/>"%str(twords/tentity)
			#rs +="Total Opinion Words : %d<br/>"%twords
			#rs +="Total Opinion : %d, Total Word : %d, Word Per Opinion : %s<hr/>"%(tentity, twords, str(twords/tentity))
	
	return HttpResponse(rs)	
	
	'''
	# Attribute Distinct
	poclist =Property.objects.values_list(
		'content', flat =True
	).exclude(
		content =""
	).filter(
		extractionPropertyID =9
	).distinct().order_by('content')
	rs +="Total Attribute : %d<br/>"%len(poclist)
	
	for c in poclist:
		rs +=c+"<br/>"
	
	rs +="<hr/>"
	'''

	'''
	for poc in poclist:
		rs +="<br/><hr/>"+str(poc)+"<br/>"
		p =Property.objects.values_list('content').filter(entityID =poc)
		k +=len(p)
		rs +=str(n)+"::"+str(p)+"<br/>"
		n +=1
	
	rs +="<br/><hr/><br/>Entity Total:"+str(n)+"<br/>"
	rs +="<br/><hr/><br/>Property Total:"+str(k)+"<br/>"
	'''
