# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HcorpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    page_title = scrapy.Field()
    headline = scrapy.Field()
    summ = scrapy.Field()
    news = scrapy.Field()
    eng_summ = scrapy.Field()
    news_body = scrapy.Field()
