#author:VincentHwuang
#Date:05-28 2017 Sun 15:00
#this file can be simply partly created with command:'scrapy genspider <name> <domain>'

from scrapy.selector import Selector
from scrapy import Spider #'Spider' is the class which we must sub-class our own classe			          #s derived from
from wikiSpider.items import Article

#"Spider" are classes that we defined and that Scrapy uses to scrape information from a 
#website(or a group of websites).They must subclass "scrapy.Spider" and define the initial
#requests(i.e. 'start_requests',even though we haven't explicitly define this method,a default one exists as well) to make,optionally how to follow links in pages,and how to parse the downloaded
#page content to extract data.
class ArticleSpider(Spider):	#define our own class 'article_spider' derived from 'Spider'
	name="article"		#identifies the Spider.It must be unique within a project
				#that is,we can't set the same name for different Spiders.
	allowed_domains=["en.wikipedia.org"]
	start_urls=["http://en.wikipedia.org/wiki/Main_Page",
		"http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
	
	def parse(self,response):
		item=Article()
		title=response.xpath('//h1/text()')[0].extract()
		print ("Title is:"+title)
		item['title']=title
		return item
