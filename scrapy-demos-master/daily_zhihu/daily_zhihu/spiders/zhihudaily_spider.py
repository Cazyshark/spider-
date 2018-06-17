# -*- coding:utf-8 -*-
# 知乎日报对页面的处理要比自己想象的还要麻烦点
# 明天早上再来决定使用

from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from v2ex.items import V2ExItem
from scrapy.exceptions import CloseSpider


class zhihudaily(Spider):
    name = 'zhihudaily'

    allowed_domains = ['daily.zhihu.com']

    start_urls = ['http://daily.zhihu.com']

    def parse(self, response):
