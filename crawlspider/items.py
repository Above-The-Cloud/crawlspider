# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Xinli001SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    cover = scrapy.Field()
    desc = scrapy.Field()
    text = scrapy.Field()
    source = scrapy.Field()
    org_id = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    meta1 = scrapy.Field()
    meta2 = scrapy.Field()
