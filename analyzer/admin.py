from django.contrib import admin
from analyzer.models import *
# Register your models here.

class AnalystAdmin(admin.ModelAdmin):
	pass
	

class PreprocessExportDataAdmin(admin.ModelAdmin):
	pass
	
	
class PreprocessAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(Analyst, AnalystAdmin)
admin.site.register(PreprocessExportData, PreprocessExportDataAdmin)
admin.site.register(Preprocess, PreprocessAdmin)