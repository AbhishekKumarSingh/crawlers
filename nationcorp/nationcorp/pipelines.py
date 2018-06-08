# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch import Elasticsearch

class NationcorpPipeline(object):
    def __init__(self):
        # open a connection
        self.es = Elasticsearch()

    def process_item(self, item, spider):
        # make link as a unique key
        d_item = dict(item)
        hash_name = item['link']

        self.es.index(index="hi-sent-summ-index1", doc_type="hi_sent_summ1", id=hash_name,
                body=d_item, timeout=20)
        return item
