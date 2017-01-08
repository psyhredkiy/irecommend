# -*- coding: utf-8 -*-
from scrapy.http import  Request
from feedback.items import FeedbackItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IreSpider(CrawlSpider):
    name = "MeineLiebe"
    allowed_domains = ["irecommend.ru"]
    start_urls = [
        'http://irecommend.ru/taxonomy/term/393347%20930502/reviews',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=1',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=2',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=3',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=4',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=5',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=6',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=7',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=8',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=9',
       'http://irecommend.ru/taxonomy/term/393347%20930502/reviews?page=10',
    ]

    rules = [
        #Rule(LinkExtractor(
        #allow=['/reviews\?page=d*']) ,
        #callback='parse_page',
        #follow=True,),

        Rule(LinkExtractor(
        restrict_xpaths=('//*[@class="views-field-teaser"]/a'),
        allow=['/content/']) ,
        callback='parse_product_page' ,
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

     #Request(url=response.url , callback='parse_f')

    #def parse_f(self,response):
        #item = FeedbackItem()
        #item['url']= response.selector.xpath('//div[@class="items list"]/a[@class="more"]').extract()
        #yield item


