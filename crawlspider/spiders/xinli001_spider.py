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
            yield scrapy.Request(url=item['link'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item=response.meta['item']
        target = response.xpath("//div[@class='yxl-editor-article ']")
        item['text'] = response.xpath("//div[@class='yxl-editor-article ']").extract_first()
        item['author'] = target.xpath("./h6[-4]/text()").extract_first()
        yield item

