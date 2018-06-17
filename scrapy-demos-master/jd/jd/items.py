# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JdbookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    '''
    product_url=Field()
    image_url=Field()
    intro=Field()
    meta=Field()

    price=Field()
    comment_rate=Field()
    '''

    product_url = Field()
    image_url = Field()

    title = Field()
    author = Field()
    price = Field()
    pub_date = Field()

'''
create table jd(
     guid CHAR(32) PRIMARY KEY,
     product_url TEXT,
     image_url TEXT
     ) DEFAULT CHARSET=utf8;
'''


class JdcomputerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    product_url = Field()
    image_url = Field()

    title = Field()
    meta = Field()
    price = Field()
    comment_count = Field()
