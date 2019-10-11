# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

import requests

class SpiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name=='xinli001_spider':
            # params={
            #     "cover":item["cover"],
            #     "desc": item["desc"],
            #     "text": item["text"],
            #     "source	": item["source"],
            #     "org_id": item["org_id"],
            #     "link": item["link"],
            #     "author": item["author"],
            #     "meta2": json.dumps(item["meta2"]),
            # }
            # url="http://127.0.0.1:8000/service/articles/create"
            # r=requests.post(url,params)
            print(item['desc'])
            # print(r.text)
            return item

        else:
            return item

