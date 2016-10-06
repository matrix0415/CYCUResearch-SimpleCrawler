from numpy import save
from numpy import array
from numpy import multiply
from ntpath import basename
from os import listdir, system
from os.path import join, getsize, abspath as abs
from multiprocessing import Process
from scipy import transpose as transarray
from sklearn import svm, cross_validation as cv
from sklearn.feature_extraction.text import HashingVectorizer as hv
from sklearn.feature_extraction.text import TfidfTransformer as tfidf
from sklearn.feature_extraction.text import TfidfVectorizer as tfidfVec
from libs.stringL import nltkL
from libs.stringL import removeNewlineL as rmNewLine
from libs.stringL import removeRedundentSpaceL as rmReduSpa

def analysisAndSave(fname, wfnameList, nltk):
	num =0
	skip =0

	lines = [rmReduSpa(rmNewLine(line)) for line in open(fname, "r").readlines()]
	linesnum =len(lines)
	
	for line in lines:
		rs =nltk.englishCorpusLemma(line, 0.7)
		nowline =lines.index(line)
		
		if rs[0]:
			num +=1
			string =nltk.posTaggerFilter(
				rs[1], ["NN", "NNS", "NNP", "NNPS", 			#Noun
						"JJ", "JJR", "JJS", 					#Adj
						"RB", "RBR", "RBS", 					#Adv
						"VB", "VBD", "VBN", "VBP", "VBZ"])		#Verb
			
			for file in wfnameList:
				file.write(string+"\n")
				print("%s\t%d/%d:\t%d\tW>>>\t%s"%(basename(fname), nowline, linesnum, num, line[:30]))
			
		else:
			skip +=1
			print("%s\t%d/%d:\t%d\tS|||"%(basename(fname), nowline, linesnum, skip))
	
	
if __name__ =="__main__":
	jobs =[]
	execBool =[]
	datapath =abs("dataset/Hotels.com/")
	sourcedatasetpath =join(datapath, "classified")
	cleandatasetpath =join(datapath, "filter")
	ngramdatasetpath =join(datapath, "ngram")
	nltk =nltkL(abs("../venv/nltk_data"))

	execBool.append("n")#input("Whether you want to filter the corpus or not? (y/n)"))
	execBool.append("n")#input("Whether you want to n-gram the corpus or not? (y/n)"))
	execBool.append("y")#input("Whether you want to calculate the first time of TFIDF for tokens or not? (y/n)"))

	if execBool[0].lower() =="y":
		system("mkdir "+cleandatasetpath)
		flist =[f[1] for f in sorted(
				[[getsize(join(sourcedatasetpath, f)), f] for f in listdir(sourcedatasetpath)]
		)]


		for fname in flist:
			wfnameList =[]
			f =fname.split("_")

			if float(f[1])>3:
				wfnameList.append(open(join(cleandatasetpath, "corpus_%d_%s_%s_%s"%(1, f[0], f[2], "pos")), 'a'))

				if float(f[1])>4:
					wfnameList.append(open(join(cleandatasetpath, "corpus_%d_%s_%s_%s"%(2, f[0], f[2], "pos")), 'a'))

			elif float(f[1])<3:
				wfnameList.append(open(join(cleandatasetpath, "corpus_%d_%s_%s_%s"%(1, f[0], f[2], "neg")), 'a'))

				if float(f[1])<2:
					wfnameList.append(open(join(cleandatasetpath, "corpus_%d_%s_%s_%s"%(2, f[0], f[2], "neg")), 'a'))

			elif float(f[1])==3:
				wfnameList.append(open(join(cleandatasetpath, "corpus_%d_%s_%s_%s"%(2, f[0], f[2], "neu")), 'a'))

			p =Process(target =analysisAndSave, args =(join(sourcedatasetpath, fname), wfnameList, nltk))
			p.start()
			jobs.append(p)

			if len(jobs) ==20:
				for job in jobs:
					job.join()

				jobs =[]

	if execBool[1].lower() =="y":
		system("mkdir "+ngramdatasetpath)
		flist =[f[1] for f in sorted(
				[[getsize(join(cleandatasetpath, f)), f] for f in listdir(cleandatasetpath)]
		)]

		for f in flist:
			ngram =[]
			fcontent =open(join(cleandatasetpath, f), 'r').read()

			for i in range(1, 5):
				ngram +=[' '.join(ngram) for ngram in nltk.string2ngram(fcontent, i)]

			fw =open(join(ngramdatasetpath, f+"_ngram"), 'w')
			fw.write(str(ngram))
			fw.close()
			print("Finish: ", f)

	if execBool[2].lower() =='y':
		n =0
		k =1000
		corpus =[]
		target =[]
		arange =[]
		corpusFLst =[fpath for fpath in listdir(cleandatasetpath)]

		for corpusF in corpusFLst:

			if corpusF.split("_")[4] =="pos":
				corpus +=open(join(cleandatasetpath, corpusF), 'r').readlines()[:k]
				target +=[n]*k
				for i in range(k):
					arange.append([5])

			elif corpusF.split("_")[4] =="neg":
				corpus +=open(join(cleandatasetpath, corpusF), 'r').readlines()[:k]
				target +=[n]*k
				for i in range(k):
					arange.append([1])
			'''
			elif corpusF.split("_")[4] =="neu":
				corpus +=open(join(cleandatasetpath, corpusF), 'r').readlines()[:k]
				target +=[n]*k
				for i in range(k):
					arange.append([1])
			'''
			#corpus +=open(join(cleandatasetpath, corpusF), 'r').readlines()[:k]
			#target +=[n]*k
			n +=1

		print(array(arange))
		print(array(arange).shape)

		target =array(target)
		print(len(corpusFLst))
		print(len(target))
		print(len(corpus))
		print(len(set(target)))
		print(target.shape)
		from time import sleep
		sleep(5)
		'''
		vec =tfidfVec(ngram_range =(1, 3), norm ='l1', use_idf =True, smooth_idf =False)
		trans =vec.fit_transform(corpus)

		feature =vec.get_feature_names()
		transary =transarray(trans.toarray())

		#print(vec.idf_)
		#print(transary)
		#print(len(transary))
		'''
		#target =[fpath for fpath in listdir(cleandatasetpath)]
		model =svm.SVC(verbose =True, cache_size =500)
		hvModel = hv(n_features=10)#, ngram_range =(1, 3), norm ='l1')
		tfidfModel =tfidf()

		counts =hvModel.transform(corpus).toarray()
		vec =tfidfModel.fit_transform(counts).toarray()
		vec =multiply(vec, arange)
		rs =cv.cross_val_score(
			model, vec, target, scoring ="accuracy", cv =20, n_jobs =10, pre_dispatch =10
		).mean()

		print(rs)

		'''
		wf =open(join("corpus1.text"), "w")
		for word in feature:
			lst =[]
			key =feature.index(word)
			lst.append(word)
			lst.append([i for i in transary[key]])
			wf.write(str(lst)+";\n")
			print(word)
		wf.close()
		'''