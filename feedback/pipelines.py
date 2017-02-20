# -*- coding: utf-8 -*-
import re
from scrapy.selector import  Selector
from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(st,'html.parser')
        for img in soup('img'):
            img.replace_with(img['alt'])
        item['text'] = soup
        return item
