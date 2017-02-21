# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeedbackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    site = scrapy.Field()
    user = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    type = scrapy.Field()


