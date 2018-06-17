# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from jd.items import JdbookItem, JdcomputerItem
from scrapy.exceptions import CloseSpider
import re

# 一开始按照自己的预想是要抓取 m.jd 的数据，但是最终实现的不是太好……
# 直接抓取网页版的吧
'''
class jd(CrawlSpider):
    name='jd'

    allowed_domains=['m.jd.com']

    start_urls=['http://m.jd.com']

    rules=[
    Rule(sle('item\.m\.jd\.com/product/[0-9]+\.html'),callback='parse_jd'),

    ]

    def parse_jd(self,response):

        sel=Selector(response)
        sel.xpath('/html')
        items=[]

        for site in sites:
            item=JdItem()

            item['product_url']=response.url 
            item['image_url']=site.xpath('//img[@src]')

            items.append(item)
        return items
'''


class jd_book(CrawlSpider):
    name = 'jd_book'

    allowed_domains = ['e.jd.com']

    start_urls = ['http://e.jd.com/ebook.html']

    rules = [
        Rule(sle(allow=(u'e.jd.com/\d+\.html')), callback='parse_jdbook')

    ]

    def parse_jdbook(self, response):
        items = []

        sel = Selector(response)

        sites = sel.xpath('/html')

        for site in sites:
            item = JdbookItem()

            item['product_url'] = response.url
            item['image_url'] = site.xpath(
                '//div[@id="preview"]/div/img[@src]').re(r'src="(.*?)" jqimg')

            item['title'] = site.xpath('//div[@id="name"]/h2/text()').extract()
            item['price'] = site.xpath(
                '//div[@id="name"]//span[@class="price"]/text()').extract()
            item['author'] = site.xpath(
                '//div[@id="name"]//ul[@id="summary"]/li[1]//a/text()').extract()

            # 时间标杆可能不同
            temp = site.xpath(
                '//div[@id="name"]//ul[@id="summary"]/li[4]/text()').extract()
            if temp:
                item['pub_date'] = site.xpath(
                    '//div[@id="name"]//ul[@id="summary"]/li[4]/text()').extract()
            else:
                item['pub_date'] = site.xpath(
                    '//div[@id="name"]//ul[@id="summary"]/li[3]/text()').extract()

            items.append(item)
            if(len(items) > 20):
                raise CloseSpider('enough')

            return items


class jd_computer(CrawlSpider):
    name = 'jd_computer'

    allowed_domains = ['jd.com']  # start_urls和实际的产品网页发生冲突

    start_urls = ['http://diannao.jd.com']

    rules = [
        Rule(sle(allow=(u'item.jd.com/\d+\.html')), callback='parse_jdcomputer')
    ]

    def parse_jdcomputer(self, response):
        items = []
        sel = Selector(response)

        sites = sel.xpath('/html')

        for site in sites:
            item = JdcomputerItem()

            item['product_url'] = response.url
            item['image_url'] = site.xpath(
                '//div[@id="preview"]/div/img[@src]').re(r'src="(.*?)" alt')
            item['title'] = site.xpath('//div[@id="name"]/h1/text()').extract()

            # price和comment_count是Ajax返回json所对应的内容
            # 这一部分需要参考SO上的
            # 或者用 Scrapyjs https://pypi.python.org/pypi/scrapyjs/0.1.1
            item['price'] = site.xpath(
                '//div[@id="summary-price"]//strong[@id="jd-price"]/text()').extract()
            # item['meta']=site.xpath('//div[@id="itemInfo"]/div/div/text()').extract()
            item['comment_count'] = site.xpath(
                '//div[@id="comment-count"]//a/text()').extract()

            items.append(item)
        return items
