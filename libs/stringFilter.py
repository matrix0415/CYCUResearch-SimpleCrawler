from re import sub
from nltk import word_tokenize
from pattern.vector import Document, Model, TFIDF
from pattern.en import parse, Sentence, lemma, suggest

from mining.models import *

class stringFilter:
	
	def settingWebsiteID(self, websiteID):
		self.websiteID =websiteID
	
	def removeRedundentSpace(self, string):
		return sub(' +',' ', string)
	
	# return clean string
	def regexFilter(self, string):
		return " ".join(sub(r"[^A-Za-z\s]+"," ", string.lower()).split()).strip()
	
	def wordLemma(self, word):
		return lemma(word)
	
	def spellingSuggest(self, word):
		return suggest(word)[0][0]
		
	def wordCleaner(self, stopwordsString, string):
		sw =word_tokenize(stopwordsString)
		string =self.regexFilter(string)
		wl =word_tokenize(string)
		#w = " ".join([w for w in wl if w not in sw])
		returnList =[]
		for w in wl:
			if w not in sw:
				returnList.append(self.wordLemma(w))
		w = " ".join(returnList)
		
		return w		
		
	def tfxidf(self, doclist):
		document = Document(string, stopwords = True, language = 'en')
		return document.keywords()
		#print count(string, stemmer=LEMMA)
