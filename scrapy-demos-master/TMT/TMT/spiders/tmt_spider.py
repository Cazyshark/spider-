# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from TMT.items import TmtItem
from scrapy.exceptions import CloseSpider


class tmtSpider(CrawlSpider):
    name = 'tmt'

    allowed_domains = ['www.tmtpost.com']

    start_urls = ['http://www.tmtpost.com/lists/hot_list']

    rules = [
        # 人们话题一共有5页，每页10篇文章
        Rule(sle(allow=('www.tmtpost.com/hot/\d+')), follow=True),
        Rule(sle(allow=('www.tmtpost.com/\d+.html')), callback='parse_tmt')
    ]

    def parse_tmt(self, response):
        items = []

        sel = Selector(response)

        sites = sel.xpath('/html')

        for site in sites:
            item = TmtItem()

            item['product_url'] = response.url
            item['title'] = site.xpath('//article/h1/text()').extract()

            # web上使用 Xpath Checker可以用//article//span[@class="time"]/text()来提取出时间
            # 但Scrapy抓取却无法抓取到,并且它也不属于js生成内容，interesting
            item['pub_date'] = site.xpath(
                '//div[@class="post-info"]/span[2]/text()').extract()
            item['intro_content'] = site.xpath(
                '//p[@class="post-abstract"]/text()').extract()

            items.append(item)
        return items
