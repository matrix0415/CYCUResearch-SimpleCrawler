def englishCheckerL(tokens, wordList):	
	rs =[False, ]
	falseWord =0
	limitGate =0.3
	tokenLen =len(tokens)
	
	if tokenLen !=0:
		for token in tokens:
			if token not in wordList:
				falseWord +=1
		
		if limitGate >= (falseWord/tokenLen):
			rs.append(tokens)
			rs[0] =True
	
	return rs
	
	
def englishPosTaggerFilterL(postaggerList, allowPos):
	return [i[0] for i in postaggerList if i[1] in allowPos]
	
	
def englishNgramConvertToSuitForPos(ngram):