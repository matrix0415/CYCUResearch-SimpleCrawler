from django.contrib import admin
from crawler.models import *

class WebsiteAdmin(admin.ModelAdmin):
	list_display =['name', 'datasetSource', 'canExtract', 'checkDataset','Extracted', 'enable']
	list_editable =['canExtract', 'enable']
	readonly_fields =('checkDataset','datasetLocation', 'datasetFileNum', 'Extracted',)

class CrawlPropertyAdmin(admin.ModelAdmin):
	list_display =['websiteID', 'url', 'nJobs']
	
class ExtractionEntityAdmin(admin.ModelAdmin):
	list_display =['id', 'websiteID', 'name', 'entitySelector']	
	
class ExtractionPropertyAdmin(admin.ModelAdmin):
	list_display =['id', 'extractionEntityID', 'name', 'propertySelector']
	
class EntityAdmin(admin.ModelAdmin):
	list_display =['websiteID', 'extractionEntityID', 'datetime', 'used']
	readonly_fields =('websiteID', 'extractionEntityID', 'content', 'datasetPath', 'used')
	search_fields =['id', ]
	
class PropertyAdmin(admin.ModelAdmin):
	list_display =['entityID', 'extractionPropertyID', 'content']
	readonly_fields =('entityID', 'extractionPropertyID', 'content')
	search_fields =['entityID__id', ]
	list_filter =['extractionPropertyID', ]

admin.site.register(Website, WebsiteAdmin)	
admin.site.register(CrawlProperty, CrawlPropertyAdmin)
admin.site.register(ExtractionProperty, ExtractionPropertyAdmin)	
admin.site.register(ExtractionEntity, ExtractionEntityAdmin)	
admin.site.register(Entity, EntityAdmin)
admin.site.register(Property, PropertyAdmin)	

'''
from mining.models import *

from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter


# For instance admin page list_filter
class websiteAdmin(admin.ModelAdmin):
	list_display =[
		'name', 'url', 
		'Scraped', 'Extracted', 'Flatted', 'Tfidf',
		'canScraping', 'canExtract', 'canFlattening', 'canTfidf'
	]	
	
	list_editable =('canScraping', 'canExtract', 'canFlattening', 'canTfidf')	
	
	readonly_fields =(
		'ratingMin', 'ratingMax', 'ratingAvg', 'ratingStdDev', 
		'minRatingCommentRowCount', 'maxRatingCommentRowCount', 
		'minRatingAvailableCommentCount', 'maxRatingAvailableCommentCount',
		'totalOpinionsCount', 'totalAvailableOpinionsCount', 
		'Scraped', 'Extracted', 'Flatted'
	)
	
	fieldsets =(
		("Basic Information", {
			'fields': ('name', 'url', 'urlParameter')
		}),
		("Scrape Range Setting", {
			'fields': ( 'rangetart', 'rangeend', 'countIncreaseRange', 'startPageOrCount', ''maxPageOrCount', 'countIncreasePage')
		}),	
		("Advanced Setting (Optional)", {
			'fields': ( 'page404', 'mustExistSoupSelector', 'getHtmlSoupSelector')
		}),	
		("Website Statistic (System Generate Parameter, Readonly)", {
			'fields': ('ratingMin', 'ratingMax', 'ratingAvg', 'ratingStdDev', 'minRatingCommentRowCount', 'maxRatingCommentRowCount', 'minRatingAvailableCommentCount', 'maxRatingAvailableCommentCount', 'totalOpinionsCount', 'totalAvailableOpinionsCount')
		}),
		("Function Status (Readonly)", {
			'fields': ('Scraped', 'Extracted', 'Flatted')
		}),		
		("Function Switch", {
			'fields': ('canScraping', 'canExtract', 'canFlattening')
		}),			
	)	
	
class scrapeHTMLAdmin(admin.ModelAdmin):
	list_display =['conditionName', 'soupSelector', 'cleanWords', 'getDataFromHTMLAttribute', 'splitData','enable']	
	list_filter = ('enable',)
	list_editable =('enable',)
	fieldsets =(
		("Basic Setting", {
			'fields': ('conditionName', 'soupSelector', 'cleanWords','getDataFromHTMLAttribute', 'splitData', 'enable')
		}),("Advanced Setting (Optional)", {
			'fields': ( 'attributeName', 'splitDataFormate', 'refuseData')
		}),	
	)
	

class webScrapeMappingAdmin(admin.ModelAdmin):
	list_display =['id', 'websiteID', 'name', 'dataOutputMean', 'dataInputType','scrapeHTML', 'used','enable']
	list_editable =('enable',)
	list_filter = ('websiteID', 'scrapeHTML', 'dataOutputMean')
	
	
admin.site.register(website, websiteAdmin)
'''