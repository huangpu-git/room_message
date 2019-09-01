# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RoomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    community_name = scrapy.Field()
    area_name = scrapy.Field()

    hu_xing = scrapy.Field()
    mian_ji = scrapy.Field()
    chao_xiang = scrapy.Field()
    zhuang_xiu = scrapy.Field()
    dian_ti = scrapy.Field()

    di_ya = scrapy.Field()
    yong_tu = scrapy.Field()
