# -*- coding: utf-8 -*-
import scrapy
from room.items import RoomItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/pg{}/'.format(num) for num in range(1, 3)]

    def parse(self, response):
        all_url = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for url in all_url:
            yield scrapy.Request(url, callback=self.parse_info)


    def parse_info(self, response):
        price = response.xpath(
            'concat(//span[@class="total"]/text(),//span[@class="unit"]/span/text())').extract_first()
        community_name = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        area_name = response.xpath('string(//div[@class="areaName"]/span[2])').extract_first()

        base = response.xpath('//div[@class="base"]/div[@class="content"]/ul')
        hu_xing = base.xpath('./li[1]/text()').extract_first()
        mian_ji = base.xpath('./li[3]/text()').extract_first()
        chao_xiang = base.xpath('./li[7]/text()').extract_first()
        zhuang_xiu = base.xpath('./li[9]/text()').extract_first()
        dian_ti = base.xpath('./li[last()-1]/text()').extract_first()

        transaction = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul')
        di_ya = transaction.xpath('./li[last()-1]/span[2]/text()').extract_first().strip()
        yong_tu = transaction.xpath('./li[4]/span[2]/text()').extract_first()

        item = RoomItem()
        item['price'] = price
        item['community_name'] = community_name
        item['area_name'] = area_name

        item['hu_xing'] = hu_xing
        item['mian_ji'] = mian_ji
        item['chao_xiang'] = chao_xiang
        item['zhuang_xiu'] = zhuang_xiu
        item['dian_ti'] = dian_ti

        item['di_ya'] = di_ya
        item['yong_tu'] = yong_tu

        yield item
