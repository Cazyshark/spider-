# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  requests

class ApplePipeline(object):
    def process_item(self, item, spider):
        url='http://qq.yh31.com'+item['addr']
        response=requsets.get(url)
        response.encoding='utf-8'\
        with open('C:\\Users\\Administrater\\Desktop\\spider\\apple\\data'%item['name'],wb)as ft:
            ft.write(response.content)


