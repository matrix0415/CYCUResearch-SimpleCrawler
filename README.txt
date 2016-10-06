System Environment ===========================

Operation System:	Ubuntu 13.04 Server (or More, non-GUI)
Python Version:		Python 2.7 (or More, under the 3.0 version)


Data Flow Diagram ============================

1. WEB HTML PAGES >> 2. WebpageCollection(HTML Type) >> 3. Instance(HTML Type) >> 4. Instance(Information)

1. WEB HTML PAGES: 
2. WebpageCollection(HTML Type):
3. Instance(HTML Type):
4. Instance(Information):


Config Setup Diagram===========================

1. Websites >> 2. Stop words >> 3. Scrape htmls >> 4. Web scrape mappings


Step by Step ==================================

Step 1, Setting Environment:
	1. Execute AutoConfigEnv.py
		CMD: sudo python AutoConfigEnv.py
				
Step 2, Syncdb
	1. change dictionary into project
		CMD: cd TextMiningProgram
		
	2. Execute AutoConfigProject.py
		CMD: python AutoConfigProject.py
		
Step 3, Runserver
	1. Execute manage.py with runserver
		CMD: python manage.py runserver 0.0.0.0:5000
		
Step 4, Config Website Scrapy
	1. Open Your Browser with IP Address and Keyin your url with port number
	
	2. Open Website Menu to Create Website which you want to scrapy and analysis
		2-1. Menu: Mining->Websites
		2-2. Add Website
			Remark:
				->URL: is refer to Website URL, but something need to be remind. URL need to follow the rules of the project, for example
				Original: http://www.imdb.com/title/tt0993846/reviews-index?start=0
				Change Into: http://www.imdb.com/title/tt%d/reviews-index?start=%d
				
				
				->Rangestart & Rangeend & CountIncreaseRange: are refer to URL Parameter one, for example:
					http://www.imdb.com/title/tt0993846/reviews-index?start=0
					tt0993846 is the Range, and you can setting Rangestart and Rangeend as where the range begin and end, and CountIncreaseRange is refer to the Increase Count of Range, for example, if the Rangestart is setting as 100 and the Rangeend is setting as 200 and CountIncreaseRange is setting as 10, The range will increase 10 every time and you can get the pages like 100, 110, 120... and so on.
				
				->StartPageOrCount & MaxPageOrCount & CountIncreasePage: are refer to URL Parameter two, for example: http://www.imdb.com/title/tt0993846/reviews-index?start=0
				PageOrCount is 0
				
				->URL Parameter: Nothing
				
				->Page404: 404 page url
				
				->MustExistSoupSelector: Component must stay on the html page 
				
				->GetHtmlSoupSelector: Get html component
				
				->CanAnalysis: Can Analysis the html page
				
				->CanScraping: Can Scraping the html page
		
				
		2-3. Execute the URL (http://youripaddress/scraping) and it will run automatically and save the html page into webpageCollection
		

Step 5, Extract the Information from HTML DOC 
	1. Setting the Stopwords (Stop words)
		Example stopwords
			i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now . , " ’ “ ” ? ! @ # $ % & - ; ( ) [ ] { }
	
	2. Setting the Scrape Condition (Scrape htmls)
		->ConditionName: 
		
		->SoupSelector:
		
		->CleanWords:
		
		->GetDataFromHTMLAttribute:
		
		->SplitData:
		
		->Enable:
		
		->AttributeName:
		
		->SplitDataFormate:
		
		->RefuseData:
		
				
	3. Mapping the Condition with Website (Web scrape mapping)
		->WebsiteID
		
		->ScrapeHTML
		
		->Name
		
		->DataInputType: Two types, Webpage HTML and Instance HTML,
		
		->DataOutputMean
		
		->Sequence
		
		->Tfidf
		
		->Enable
	
	
	4. Extract and analysis the data
		Open the url (http://youripaddress/htmlAnalysis)
		
	5. Now, Data are look like:
		
id	websiteID_id	webpageCollectionID_id	webScrapeMappingID_id	instanceKey	content	used	instanceSelfID_id 	
1708904 	1 	2002 	5 	0 	love hotel love food staff neighborhood proximity ...	0 	9559
1708905 	1 	2002 	5 	1 	four season bangkok like classic car get engine wi...	0 	9560
1708906 	1 	2002 	5 	2 	old four season best one have far genuine expedia ...	0 	9561
1708907 	1 	2002 	5 	3 	front desk housekeep concierge restaurant personne...	0 	9562
1708908 	1 	2002 	5 	4 	great location fantastic service locate near shop ...	0 	9563
1708879 	1 	2002 	4 	5 	au	0 	9564
1708874 	1 	2002 	5 	5 	excellent escape luxury thoroughly enjoy stay genu...	0 	9564
1708884 	1 	2002 	6 	5 	5.0	0 	9564
1708894 	1 	2002 	7 	5 		0 	9564
1708889 	1 	2002 	8 	5 		0 	9564
1708899 	1 	2002 	9 	5 		0 	9564
1708880 	1 	2002 	4 	6 		0 	9565
1708875 	1 	2002 	5 	6 	bad service sorry bad understatement pathetic serv...	0 	9565
1708885 	1 	2002 	6 	6 	1.0	0 	9565
1708895 	1 	2002 	7 	6 		0 	9565
1708890 	1 	2002 	8 	6 		0 	9565
1708900 	1 	2002 	9 	6 		0 	9565

	
Step 6, Store data into datawarehouse (Optional)	
	1.
	
	2.
	
	3.
	

Step 7, Tfidf
	1. 
	
	2. 
	
	3. 
	
	
	