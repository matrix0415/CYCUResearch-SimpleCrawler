from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^crawl/', 'crawler.views.crawl'),
	url(r'^extract/(?P<execType>\w+)', 'crawler.views.extract'),
	url(r'^attributecleaner/', 'crawler.views.attributeCleaner'),
	url(r'^test/', 'crawler.views.test'),
	url(r'^checker/', 'analyzer.views.checker'),
)
