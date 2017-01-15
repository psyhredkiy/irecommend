# -*- coding: utf-8 -*-
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
        #Rule(LinkExtractor(
        #allow=['/reviews\?page=d*']) ,
        #callback='parse_page',
        #follow=True,),

        Rule(LinkExtractor(
        restrict_xpaths=('//*[@class="views-field-teaser"]/a'),
        allow=['/content/']) ,
        callback='parse_comments' ,
        follow=True)

    ]

    #def parse_page(self, response):
    #    response.selector.xpath('//nobr[@class="views-field-teaser"]/a').extract()



    def parse_product_page(self, response):
        item = FeedbackItem()
        item['date'] = response.selector.xpath('//span[@class="dtreviewed"]/text()').extract()
        item['user'] = response.selector.xpath('//strong[@class="reviewer"]/a/text()').extract()
        item['title'] = response.selector.xpath('//h2[@class="summary"]/a/text()').extract()
        item['url'] = response.url
        item['site'] = IreSpider.allowed_domains
        item['text'] = response.selector.xpath('//div[@class="views-field-teaser"]/div/*/text()').extract()
        yield item




    def parse_comments(self,response):

       item = FeedbackItem()
       item['date'] = response.selector.xpath('//span[@class="dtreviewed"]/meta/@content').extract()
       item['user'] = response.selector.xpath('//strong[@class="reviewer"]/a/text()').extract()
       item['title'] = response.selector.xpath('//h2[@class="summary"]/a/text()').extract()
       item['url'] = response.url
       item['site'] = IreSpider.allowed_domains
       item['text'] = response.selector.xpath('//div[@class="views-field-teaser"]/div//*').extract()
       yield item

       sel = Selector(response)
       title = response.selector.xpath('//h2[@class="summary"]/a/text()').extract()
       sites = sel.xpath('//ul[@class="list"]/li')
       items = []
       for site in sites:
           item = FeedbackItem()

           item['url'] = response.url
           item['site'] = IreSpider.allowed_domains
           item['title'] = title
           item['text'] = site.xpath('div[@class="txt"]//*').extract()
           item['user'] = site.xpath('div/a/text()').extract()
           item['date'] = site.xpath('div/span/@title').extract()

           items.append(item)

       for item in items:
           yield item


     #Request(url=response.url , callback='parse_f')

    #def parse_f(self,response):
        #item = FeedbackItem()
        #item['url']= response.selector.xpath('//div[@class="items list"]/a[@class="more"]').extract()
        #yield item


