# -*- coding: utf-8-*-

class textAnalysis(object):
	def sentenceVector(self, sentence):
		from pattern.en import parse, Sentence
	
		sentenceSentence =Sentence(parse(sentence))
		sentenceVector =Vector(count(docSentence, stemmer=LEMMA, language ='en', stopwords =True))
		
		return sentenceVector
	
	
	def normalizeVector(self, vector):
		from pattern.vector import normalize
		
		normalV =normalize(minV)
		
		return vector
	
'''
from mining.models import *

from django import db
from django.db.models import Q
from django.db import connection
from pattern.en import parse, Sentence
from pattern.vector import count, LEMMA, Document, Vector, tfidf, Model, TFIDF


def cleanData(request):
	delList =[]
	cursor = connection.cursor()
	cursor.execute("SELECT webpageCollectionID_id, COUNT(id) as c FROM mining_instance GROUP BY webpageCollectionID_id, instanceKey ORDER BY c")
	row = cursor.fetchall()
	
	for r in row:
		if r[1] <5:
			cursor.execute("Delete FROM mining_instance WHERE webpageCollectionID_id ="+str(r[0]))
		elif r[1]>5:
			print r[0]
	
	return HttpResponse(str(row))
def tfidfView(request):
	rs =""
	hstr =""
	lstr =""
	
	high =instance.objects.values('webpageCollectionID', 'instanceKey').filter(scrapeHTMLID =4, content=5.0)
	for h in high:
		ho =instance.objects.values('content').filter(Q(scrapeHTMLID =1)|Q(scrapeHTMLID =6), webpageCollectionID =h['webpageCollectionID'], instanceKey =h['instanceKey'])
		for hs in ho:
			hstr +=hs['content']+" "
			
	low =instance.objects.values('webpageCollectionID', 'instanceKey').filter(scrapeHTMLID =4, content=1.0)
	low2 =instance.objects.values('webpageCollectionID', 'instanceKey').filter(scrapeHTMLID =4, content=2.0)
	
	for l in low:
		lo =instance.objects.values('content').filter(Q(scrapeHTMLID =1) | Q(scrapeHTMLID =6), webpageCollectionID =l['webpageCollectionID'], instanceKey =l['instanceKey'])
		for ls in lo:
			lstr +=ls['content']+" "
	for l in low2:
		lo =instance.objects.values('content').filter(Q(scrapeHTMLID =1) | Q(scrapeHTMLID =6), webpageCollectionID =l['webpageCollectionID'], instanceKey =l['instanceKey'])
		for ls in lo:
			lstr +=ls['content']+" "
	
	print "TFIDF Start"	
	
	hsen =Sentence(parse(hstr))
	lsen =Sentence(parse(lstr))
	
	print "Vector Start"
	
	hv =Vector(count(hsen, stemmer=LEMMA, language ='en', stopwords =True))
	lv =Vector(count(lsen, stemmer=LEMMA, language ='en', stopwords =True))
	
	print "TFIDF Compute Start"
	
	m =tfidf([hv, lv], base=10)
	
	print "LOOP Start"
	rs +=str(m)+"<br/><br/><br/><br/><br/><br/><br/><br/>"
	for ii in m:
		#rs +=str(ii)+"<br/><br/><br/><br/><br/><br/><br/><br/>"
		for iii in ii:
			if ii[iii]>3:
				rs +=str(iii)+"<br/>"
		rs +="<br/><br/><br/><br/><br/><br/><br/><br/>"
		
	#rs =hstr+"</br></br></br></br><hr/></br></br></br></br></br></br>"+lstr
	
	return HttpResponse(rs)
	
def htmlAnalysis(request):
	rs =""
	site =website.objects.values('id').filter(canAnalysis =True)
	for si in site:
		st =scrapyTools(si['id'])
		scrape =scrapeHTML.objects.values().filter(websiteID_id =si['id'], enable =True).order_by('scrapeSequence')
		
		for s in scrape:
			#rs +="<h1>%s</h1><br/><br/>"%s['name']
			for k in range(1, 500):
				if s['getHtmlSourceFromWebpageCollection']:
					print
					print
					print "Count: %d----------"%k
					print
					page =webpageCollection.objects.filter(page404 =False, enable =True, used =False).order_by('id')[1+50*(k-1):50*k]
					print type(page)
					for p in page:
						st.setScrappingInfo(p.id, p.html)
						stRs =st.scrapping(s, "")
						#if not stRs[0]:
							#rs +=str(stRs)+"<br/><br/>"
						#	pass
						#else:
						p.html =""
						p.used =True
						p.save()
						print "WebpageColletion Change()"
						print stRs
						print
					if k%3 ==0:
						print "Release Memory"
						db.reset_queries()
						
					
				elif s['getDataFromScrapeHTMLID'] !='':
					#scrape =scrapeHTML.objects.values('id').get(websiteID =s['id'], name =s['getDataFromHTML'])
					ince =instance.objects.values().filter(scrapeHTMLID =s['getDataFromScrapeHTMLID'])[1+200*(k-1):200*k]
					for i in ince:
						#rs +=str(i['id'])+"<br/>"
						st.setScrappingInfo(i['webpageCollectionID_id'], i['content'])
						stRs =st.scrapping(s, i['instanceKey'])
						#if not stRs[0]:
							#rs +=str(stRs)+"<br/><br/>"
						print s['name']
						print stRs
						print
			
			rs +="<hr/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>"
	return HttpResponse(rs)

'''