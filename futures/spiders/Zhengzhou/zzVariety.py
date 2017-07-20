#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : zzVariety
# Fatures:
# Author : qianyong
# Time   : 2017-06-26 17:51
# Version: V0.0.1
#

from scrapy.spiders import Spider
from futures.items.day_quotes import ZhengZhouVarietyItem
class ZhengZhouVariety(Spider):
    name = 'zhengzhou_variety'

    start_urls = ['http://www.czce.com.cn/portal/jysj/qhjysj/mrhq/A09112001index_1.htm']

    def parse(self, response):
        # print(response.url)
        # print(response.text)
        row_list = response.xpath('//*/select[@name="commodity"]/option')
        for row in row_list:
            if row.xpath('text()').extract()[0] == '全部':
                pass
            else:
                item = ZhengZhouVarietyItem()
                item['code'] = row.xpath('@value').extract()[0]
                item['name'] = row.xpath('text()').extract()[0]
                yield item