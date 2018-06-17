# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from vip.items import VipItem
from scrapy.exceptions import CloseSpider


class vipSpider(CrawlSpider):
    name = 'vip'

    allowed_domains = ['m.vip.com']

    start_urls = ['http://m.vip.com']

    rules = [
        Rule(sle(allow=(u'index\.php.*')), follow=True),
        Rule(sle(allow=('m.vip.com/product.*')), callback='parse_vip'),
        Rule(sle(allow=('m.vip.com/brand.*')), follow=True),
        # Rule(sle(allow=(u'product.*')),callback='parse_vip')
    ]

    def parse_vip(self, response):
        items = []

        sel = Selector(response)

        sites = sel.xpath('/html')

        for site in sites:
            item = VipItem()

            item['product_url'] = response.url
            item['image_url'] = site.xpath(
                '//li[@style="width: 224px; display: table-cell; vertical-align: top;"]//img[@src][1]').re(r'src=(.*?) data')
            item['price'] = site.xpath(
                '//span[@class="u-detail-price"]/text()').extract()
            item['name'] = site.xpath('//h1/text()').extract()

            # item['brand']=
            # item['location']=
            # item['material']=

            items.append(item)

        return items
