# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class IreSpider(CrawlSpider):
    name = "ire"
    allowed_domains = ["irecommend.ru"]
    start_urls = ['http://irecommend.ru/taxonomy/term/393347%20930502/reviews']
    rules = [Rule(LinkExtractor(allow=['/content/']), 'parse_products')]

    def parse_products(self, response):

        SItem.url = response.url