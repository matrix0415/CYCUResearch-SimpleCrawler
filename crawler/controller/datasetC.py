#
#  @importFromWebExportToFileC
#  @param  siteName 	<string> website.name
#  @param  urlList 	<list> 	["url", "url", ...]
#  @param  page404  	<string> CrawlProperty.page404Path
#  @return None	 	
#  @brief  crawl web pages and save to files.
#  
def importFromWebExportToFileC(siteName, urlList, page404):
	from os.path import join
	from crawler.libs.datasetL import fetchFromWebL, saveByFileL
	
	rs =""
	
	for id, url in urlList:
		fetchRsList =fetchFromWebL(url, page404)
		fname =join(siteName, str(id))
		
		if fetchRsList[0]:
			saveRs =saveByFileL(fname, fetchRsList[1])
			rs ="%s:\t%s"%(fname, str(saveRs))
			
		else:
			rs ="%s:\t%s"%(fname, str(fetchRsList))
		
		print(rs)
		

def extractFromHTMLC(fpathOrHTML, selector):
	from os.path import exists, isfile
	from libs.fileL import fileRead
	from libs.htmlL import soupSelectorL
	
	rs =[False, ]
	
	if exists(fpathOrHTML) and isfile(fpathOrHTML):	# input html file
		fcontent =fileRead(fpathOrHTML)		
		
		if fcontent[0]:
			entityRs =soupSelectorL(fcontent[1], selector)
			rs.append(entityRs[1])	
			
			if entityRs[0]:
				rs[0] =True
				
				if entityRs[1] ==[]:
					entityRs[1].append("")
					
		else:
			rs.append(fcontent[1])	
		
	else:					# input html code		
		fcontent =[True, fpathOrHTML]	
		entityRs =soupSelectorL(fcontent[1], selector)
		
		if entityRs[0]:			
			if entityRs[1] ==[]:
				content =""
			else:
				content =entityRs[1][0].get_text()
				
			rs.append(content)
			rs[0] =True
			
		else:
			rs.append(entityRs[1])		
			
	return rs
		
		
def fetchPathC(path, type):
	from os.path import join
	from libs.errorlogL import writeLogL
	
	rs =[False,]
	
	try:
		if type =="url":
			from libs.nlpLib import fetchUrl
			rs.append(fetchUrl(path))
			rs[0] =True
			
		elif type =="file":
			from os import listdir
			rs.append([join(path, f) for f in listdir(path)])
			rs[0] =True
		
	except Exception as e:
		rs.append(writeLogL("crawler.controller.datasetC.fetchPath", e))
		
	return rs
