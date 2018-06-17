# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class HupuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = Field()
    pub_date = Field()
    highlight_count = Field()

    title = Field()
    url = Field()
    content = Field()

'''
create table hupu(
	 guid CHAR(32) PRIMARY KEY,
     url TEXT) DEFAULT CHARSET=utf8;
'''
