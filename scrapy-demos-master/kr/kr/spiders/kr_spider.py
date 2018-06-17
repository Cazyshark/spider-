# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from kr.items import KrItem
from scrapy.exceptions import CloseSpider


class krSpider(CrawlSpider):
    name = 'kr'

    allowed_domains = ['36kr.com']

    start_urls = ['http://www.36kr.com']

    rules = [
        # 目标只是抓取首页上的文章
        Rule(sle(allow=('36kr.com/p/\d+\.html')), callback='parse_kr'),
    ]

    def parse_kr(self, response):
        items = []

        sel = Selector(response)

        sites = sel.xpath('/html')

        for site in sites:
            item = KrItem()
            item['product_url'] = response.url
            item['image_url'] = site.xpath(
                '//div[@class="single-post-header__headline"]/img').re('src="(.*?)"')
            # item['image_url']=site.xpath('//div[@class="inner"]//img[@src]').re('src="(.*?)[^wechat]"')
            item['title'] = site.xpath(
                '//div[@class="inner"]//h1[1]/text()').extract()
            item['author'] = site.xpath(
                '//div[@class="inner"]//span[@class="name"]/text()').extract()
            item['intro_content'] = site.xpath(
                '//section[@class="article"]/p[1]').extract()
            item['pub_date'] = site.xpath(
                '//div[@class="inner"]//time[@class="timeago"]/text()').extract()

            items.append(item)
        return items
