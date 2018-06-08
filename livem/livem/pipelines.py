# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch

class LivemPipeline(object):
    def __init__(self):
	self.es = Elasticsearch()

    def process_item(self, item, spider):
        d_item = dict(item)
	hash_name = item['link']

	self.es.index(index="en-sent-summ-livem", doc_type="en_sent_summ_livem", id=hash_name,
		      body=d_item, timeout=20)
	return item
