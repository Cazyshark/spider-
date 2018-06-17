# -*- coding:utf-8 -*-
from scrapy.spiders import Spider,CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from hupu.items import HupuItem
from scrapy.exceptions import CloseSpider

class hupuSpider(Spider):
	name='hupu'
	allowed_domains=['bbs.hupu.com/topic']

	start_urls=[u'http://bbs.hupu.com/topic/highlights-%d' % d for d in range(1,3)]
	'''
	rules=[
		Rule(sle(allow=(u'highlights-[\d]')),callback='parse_hupu')
	]
	'''

	def parse(self,reponse):

		sel=Selector(reponse)
		items=[]

		sites=sel.xpath('//div[@class="floor"]')
		print len(sites)
		print sites[1]
		for site in sites:
			item=HupuItem()

			item['author']=site.xpath('div/div/div/a/text()').extract()
			item['pub_date']=site.xpath('div/div/div/span[@class="stime"]/text()').extract()
			item['highlight_count']=site.xpath('div/div/div/span[@class="f444"]/font/span[@class="stime"]/text()').extract()

			item['url']=site.xpath('div//p[@class="l_w_re"]/a[@href]').re('<a href="(.*?)" target')
			item['title']=site.xpath('div//p[@class="l_w_re"]/text()').extract()

			# 最后这里还需要用re来处理<tr><td>等内容
			item['content']=site.xpath('div/table[@class="case"]').extract()
			items.append(item)

		return items


