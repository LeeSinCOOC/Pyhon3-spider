# -*- coding: utf-8 -*-
import scrapy
from Tenxun.items import TenxunItem

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?start=0']
    url = 'https://hr.tencent.com/position.php?&start='
    def parse(self,response):
        for page in range(0,281,10):
            full_url = self.url+str(page)
            yield scrapy.Request(full_url,callback=self.parseHTML)
    def parseHTML(self,response):
        item = TenxunItem()
        baselist = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for base in baselist:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]
            yield item