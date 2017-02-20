# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from scrapy.http import  Request
from feedback.items import FeedbackItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

class IreSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["irecommend.ru"]
    start_urls = [
        'http://irecommend.ru/taxonomy/term/393347%20930502/reviews',

    ]

    rules = [

        Rule(LinkExtractor(
        restrict_xpaths=('//nobr[@class="views-field-teaser"]/a'),
        allow=['/content/']) ,
        callback='parse_comments' ,
        follow=True)
            ]

    def parse_comments(self,response):

       item = FeedbackItem()
       item['date'] = response.selector.xpath('//span[@class="dtreviewed"]/meta/@content').extract()
       item['user'] = response.selector.xpath('//strong[@class="reviewer"]/a/text()').extract()
       item['title'] = response.selector.xpath('//h2[@class="summary"]/a/text()').extract()
       item['url'] = response.url
       item['site'] = IreSpider.allowed_domains
       item['text'] = response.selector.xpath('//div[@class="views-field-teaser"]//*').extract()
       yield item

       sel = Selector(response)
       title = response.selector.xpath('//h2[@class="summary"]/a/text()').extract()
       sites = sel.xpath('//ul[@class="list"]/li').extract()
       items = []

       for site in sites:
           item = FeedbackItem()
           item['url'] = response.url
           item['site'] = IreSpider.allowed_domains
           item['title'] = title
           #txt = site.xpath('/div[@class="txt"]').extract()
           sitej = "".join(site)
           sp = BeautifulSoup(sitej,'html.parser')
           soup = sp.find("div",class_="txt")
           strngs = []
           for img in soup("img"):
               img.replace_with(img['alt'])
           for string in soup.stripped_strings:
               strngs.append(string)
           strj= "".join(strngs)
           item['text'] = strj
           item['user'] =  site.xpath('div/a/text()').extract()
           item['date'] =  site.xpath('div/span/@title').extract()

           items.append(item)

       for item in items:
           yield item


