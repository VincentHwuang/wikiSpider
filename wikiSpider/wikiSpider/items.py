# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#another way
#from scrapy import Item
#from scrapy import Field

class Article(scrapy.Item):	
    	#we define a class named 'Article' derived from class 'scrapy.Item'
    	#each Scrapy Item object represents a single page on the website.
	#Obviously,we can define as many as fields as we'd like(url,content,etc.)
	#but here,we just simply collect the 'title' field from each page.
	# define the fields for your item here like:
    	# name = scrapy.Field()
	title=scrapy.Field()	#here,we just simply collectly the 'title' field 
