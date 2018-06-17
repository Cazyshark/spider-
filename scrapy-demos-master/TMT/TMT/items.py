# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TmtItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = Field()
    title = Field()
    pub_date = Field()
    intro_content = Field()
