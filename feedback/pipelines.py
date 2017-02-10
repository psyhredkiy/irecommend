# -*- coding: utf-8 -*-
import re
from scrapy.selector import  Selector
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FeedbackPipeline(object):
    def process_item(self, item, spider):
        st = ''.join(item['date'])
        i = re.sub('T.*','',st)
        item['date'] = unicode(i)
        return item


class ImageAlt(object):
    def process_item(self, item, spider):
        st = ''.join(item['text'])
        p=re.compile(r"(<img src.*alt=\")+(\W*)(\w*)(\">)")
        re2=re.sub(p,r"\3",st)
        item['text'] = Selector(text=re2).xpath('//text()').extract()
        return item
