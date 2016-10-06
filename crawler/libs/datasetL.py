#
#  @fetchFromWebL
#  @param  importPath	<string>	url
#  @param  page404Path	<string>	url
#  @return rs			<list>	[True/False, Html/Exception]
#  @brief  get html file from web by using gzip.
#  
def fetchFromWebL(importPath, page404Path):
	from urllib import request
	from libs.htmlL import CrawlHtmlL
	from libs.errorlogL import writeLogL
	
	rs =[False, ]
	
	try:
		opener = request.build_opener(CrawlHtmlL, request.HTTPHandler)
		opener.addheaders=[
                    ('Accept', 'application/json, text/javascript, */*; q=0.01'),
					('Accept-Language', 'q=0.8,en-us; q=0.5,en'),
                    ('Host', 'www.hotels.com'),
                    ('Content-Type', 'application/json; charset=UTF-8'),
                    ('Connection', 'keep-alive'),
                ]
		
		respO = opener.open(importPath)
		
		if respO.url != page404Path:
			rs.append(respO.read().decode('utf-8'))
			rs[0] =True
		
		else:
			rs.append("Redirect to page 404.")
		
	except Exception as e:
		rs.append(writeLogL("crawler.libs.datasetL.fetchFromWebL", e))
		
	return rs
	
	
def saveByFileL(fname, content):
	import time
	from os.path import dirname, abspath, join
	from libs.fileL import fileWrite
	from libs.errorlogL import writeLogL
	
	rs =[False, ]
	today =str(time.strftime("%Y%m%d%H%M%S"))
	
	try:
		path =join(abspath(dirname(dirname(dirname(__file__)))), 'dataset')
		rs =fileWrite("%s/%s_%s"%(path, fname, today), content)
		
	except Exception as e:
		rs.append(writeLogL("crawler.libs.datasetL.saveByFileL", e))
		
	return rs
		

def fetchFromLocalL(importPath):
	import os
	from libs.fileL import fileRead
	from libs.errorlogL import writeLogL
	
	fList =[]
	
	for filename in os.listdir(importFolderPath):
		try:
			f =fileRead("%s/%s"%(importFolderPath, filename))
			fList.append(f)
			
		except Exception as e:
			fList.append(writeLogL("crawler.libs.datasetL.fetchFromLocalL", e))
	
	return fList	