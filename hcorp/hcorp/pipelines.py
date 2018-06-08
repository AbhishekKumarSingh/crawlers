# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import redis
from elasticsearch import Elasticsearch

class HcorpPipeline(object):
    def __init__(self):
        # open a redis connection
        #self.rserver = redis.Redis('localhost')
	self.es = Elasticsearch()

    def process_item(self, item, spider):
        # make link as unique key
        d_item = dict(item)
        hash_name = item['link']

        #if self.rserver.sadd('news_record', hash_name):
        #    self.rserver.hmset(hash_name, d_item)
	self.es.index(index="hi-sent-summ-index", doc_type='hi-sent-summ', id=hash_name,
		body=d_item, timeout=20)
        return item
