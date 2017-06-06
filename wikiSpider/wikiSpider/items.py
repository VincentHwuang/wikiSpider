# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#Each Scrapy item object represents a single page on the website.
#Obviously,we can define as many fields as we'd like(url,content,
#header,image,etc.)
class Article(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title=scrapy.Field()	
