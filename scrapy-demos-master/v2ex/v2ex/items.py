# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class V2ExItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = Field()
    title = Field()
    author = Field()
    category = Field()
    pub_date = Field()
    reply_count = Field()

    '''
    create database scrapy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
create table v2ex(
	 guid CHAR(32) PRIMARY KEY,
     title TEXT,
     author TEXT,
     link TEXT,
     reply_count TEXT) DEFAULT CHARSET=utf8;
	'''
