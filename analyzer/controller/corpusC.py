def englishCorpusProcessC(string, nltkObj):
	from analyzer.libs.corpusL import englishCheckerL as checker
	
	rs =[False, ]
	
	
	wordList =nltk.englishWordList()
	tokens =nltk.englishTokenizer(s)
	
	rs =checker(tokensList, wordList)
	
	return rs
	
	