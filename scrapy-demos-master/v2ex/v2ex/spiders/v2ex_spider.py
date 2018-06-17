# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from v2ex.items import V2ExItem
from scrapy.exceptions import CloseSpider


class v2exSpider(CrawlSpider):
    name = 'v2ex'
    allowed_domains = ['v2ex.com']
    start_urls = [u'http://www.v2ex.com/?tab=hot']

    rules = [
        Rule(sle(allow='/t/\d+'), callback='parse_v2ex')
    ]

    def parse_v2ex(self, response):

        items = []
        sel = Selector(response)
        sites = sel.xpath('/html')
        for site in sites:
            item = V2ExItem()

            item['link'] = response.url
            item['title'] = sel.xpath('//h1/text()').extract()[0]
            

            # 不是太具有代表性，但在自己所处理的页面中都已经读取成功
            item['author'] = sel.xpath(
                '//*[@id="Main"]/div[2]/div[1]/small/a/text()').extract()
            #item['tag'] = sel.xpath(
            #    '//*[@id="Main"]/div[2]/div[1]/a[2]').extract()
            #item['pub_time'] = sel.xpath(
            #    '//*[@id="Main"]/div[2]/div[1]/small/text()').extract()[0:10]
            item['reply_count'] = sel.xpath(
                '//span[@class="gray"]/text()').extract()[0:5]

            items.append(item)

            if (len(items))>30:
            	raise CloseSpider('enouht')

        return items
