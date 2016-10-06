from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def checker(request):
	from crawler.models import Property as p
	from libs.nlpLib import nltkL, removePunctuationL
	from analyzer.controller.corpusC import englishCorpusProcessC as corpusProce
	
	eng =0
	non =0
	
	analysts =Analysts.objects.only('nltkdataPath').filter(enable =True)
	#  corpus is english
	#  n-gram
	#  pos filter
	for analyst in analysts:
		nltk =nltkL(analyst.nltkdataPath)	
		plist =list(p.objects.values_list('entityID', flat =True).filter(extractionPropertyID =11, content="1.0").distinct())
		ss =list(p.objects.values_list('content', flat =True).filter(entityID__in =plist, extractionPropertyID =16))
		
		for s in ss:
			s =removePunctuationL(s).lower().replace("genuine hotels.com guest review", "").replace("read more", "")
			rs =corpusProce(s, nltk)
			if rs[0]:
				eng +=1
			else:
				non +=1
			print(ssLen, rs[0])
			ssLen -=1
			
		print("eng : ", eng)
		print("non : ", non)		
		
	return HttpResponse("Done")
	
	
	