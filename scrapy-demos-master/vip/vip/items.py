# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class VipItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = Field()
    image_url = Field()
    price = Field()

    name = Field()
    # brand=Field()
    # locaiton=Field()
    # material=Field()
    '''
create table vip(
	 guid CHAR(32) PRIMARY KEY,
     product_url TEXT,
     price TEXT,
     name TEXT) DEFAULT CHARSET=utf8;
	'''
