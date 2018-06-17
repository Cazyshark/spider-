import scrapy
from apple.items import AppleItem
class  Myspider(scrapy.Spider):
    name='bqb'
    def start_requests(self):
        start_urls=['http://qq.yh31.com/zjbq/2920180.html',
                    'http://qq.yh31.com/zjbq/2920180_2.html']
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)




    def parse(self,response):
        img_urls=response.xpath('//img')
        a=0
        for img_url in img_urls:

            url=img_url.xpath('@src').extract()
            item=AppleItem()
            item['name']=a
            item['addr']=url[0]
            a+=1
            yield item





