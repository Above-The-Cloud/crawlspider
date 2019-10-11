import datetime
import time

import scrapy

from crawlspider.items import Xinli001SpiderItem


class Xinli001Spider(scrapy.Spider):  # 需要继承scrapy.Spider类

    name = "xinli001_spider"  # 定义蜘蛛名
    start_urls = ['https://www.xinli001.com/info']

    def parse(self, response):
        target=response.xpath("//div[@id='articleListM']/div")
        for each in target:
            item = Xinli001SpiderItem()
            item['desc']=each.xpath(".//p[@class='desc']/text()").extract_first()
            item['cover']=each.xpath(".//img").attrib['src']
            item['source']=1
            item['link']="https:"+each.xpath(".//a[1]").attrib['href']
            yield item
            # yield scrapy.Request(url=item['link'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item=response.meta['item']
        target = response.xpath("//div[@class='yxl-editor-article ']")
        item['text'] = response.xpath("//div[@class='yxl-editor-article ']").extract_first()
        item['org_id'] = item['link'].split("/")[-1]
        item['author'] = target.xpath("./h6[last()-3]/text()").extract_first()
        ctime = response.xpath("//div[@class='info']/span[1]/text()").extract_first()
        ctime=ctime[-10:]
        item['meta2']={}
        item['meta2']['org_ctime'] = int(time.mktime(datetime.datetime.strptime(ctime, "%Y-%m-%d").timetuple()))
        item['meta2']['org_like_cnt'] = int(response.xpath("//div[@class='info']/span[2]/text()").extract_first()[:-1])
        item['meta2']['org_cmt_cnt'] = int(response.xpath("//div[@class='info']/span[3]/text()").extract_first()[:-2])
        item['meta2']['org_read_cnt'] = int(response.xpath("//div[@class='info']/span[4]/text()").extract_first()[:-2])
        return item

