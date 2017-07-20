#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : HuaxiDayQoutes
# Fatures:
# Author : qianyong
# Time   : 2017-06-22 09:29
# Version: V0.0.1
#

"""
华西村日行情

从交易信息首页获取  数据日期
"""
from futures.items.day_quotes import DayQuotesItem
from scrapy.spiders import Spider
from scrapy.http import Response, Request
from urllib import parse
import re
import datetime
import time

huaxicun_item = ['乙二醇']


class HuaXiDayQuotes(Spider):
    name = 'hxcce'
    allowed_domains = ['www.hxcce.com']
    start_urls = ['http://www.hxcce.com/html/rishujutongji/list_10_1.html']
    i = 0

    def parse(self, response):
        self.i += 1
        link_list = response.css("table:nth-child(3) a::attr(href)").extract()
        for link in link_list:
            yield Request(url=parse.urljoin(response.url, link), callback=self.parse_detail)
        node = response.css(".pages li:nth-last-child(4)")
        # print node.css("a::text")
        if self.i > 1:
            pass
        else:
            if node.css("a::text").extract_first("") == '下一页':
                next_url = node.css("a::attr(href)").extract_first("")
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        new_head_list = response.css("table:nth-child(3) tr:nth-child(3) table:nth-child(1) tr:nth-child(1) td").xpath(
            'string(.)').extract()
        # head_list = list(set(head_list))
        head_list = list(set(new_head_list))
        head_list.sort(key=new_head_list.index)
        head_dict = {'品种': 'goods_name', '持仓量': 'position_volume', '今结算价': 'settlement_price',
                     '昨结算价': 'pre_settlement_price',
                     '涨跌': 'change', '交易金额': 'deal_amount', '最高价': 'highest_price', '最低价': 'lowest_price',
                     '开市价': 'open_price', '收市价': 'close_price', '总成交量': 'deal_volume', '成交量': 'deal_volume',
                     '日期': 'data_date'}
        if head_list:
            # print(head_list)

            head_list = list(map(lambda head: head_dict[head.strip()], head_list))
            # print(head_list)
            tr_list = response.css('table:nth-child(3) tr:nth-child(3) table tr:not(tr:nth-child(1))').css(
                'tr:not(tr:last-child)')
        else:
            tr_list = []
        index = 0
        if tr_list:
            for tr in tr_list:
                item = tr.css('td').xpath('string(.)').extract()
                item = list(map(lambda item: item.strip(), item))

                goods_name = self.get_goods_name(item[head_list.index('goods_name')])
                delivery_month = self.get_date(item[head_list.index('goods_name')])
                if goods_name in huaxicun_item:
                    # print(item)
                    # print('乙二醇 === item')

                    new_item = DayQuotesItem()
                    new_item['goods_name'] = goods_name
                    new_item['delivery_month'] = delivery_month
                    new_item['open_price'] = item[head_list.index('open_price')]
                    new_item['highest_price'] = item[head_list.index('highest_price')]
                    new_item['lowest_price'] = item[head_list.index('lowest_price')]
                    new_item['close_price'] = item[head_list.index('close_price')]
                    new_item['pre_settlement_price'] = item[head_list.index('pre_settlement_price')]
                    new_item['settlement_price'] = item[head_list.index('settlement_price')]
                    new_item['change_1'] = item[head_list.index('change')]
                    new_item['change_2'] = float(item[head_list.index('settlement_price')]) - float(
                        item[head_list.index('pre_settlement_price')])
                    new_item['deal_volume'] = item[head_list.index('deal_volume')]
                    new_item['position_volume'] = item[head_list.index('position_volume')]
                    new_item['deal_amount'] = item[head_list.index('deal_amount')]
                    new_item['quote_date'] = item[head_list.index('data_date')]
                    yield new_item
                    # print(head_list)
                    # item_loader = HxcItemLoader(item=HxcspiderItem(), response=response)
                    # item_loader.add_value("url", response.url)
                    # print(response.url)
                    # item_loader.add_value("url_object_id", get_md5(response.url+str(index)))
                    # print(get_md5(response.url+str(index)))
                    # print(response.url+str(index))
                    # index += 1
                    # for i in range(len(head_list)):
                    #     item_loader.add_value(head_list[i], item[i])
                    #     if(head_list[i] == 'goods_name'):
                    #         item_loader.add_value('delivery_date', item[i])
                    #     # print(item[i])
                    #
                    # hxc_item = item_loader.load_item()
                    # # print(hxc_item)
                    # yield hxc_item

    def get_date(self, value):
        # print(value)
        match_re = re.match(".*?(\d{2})(\d{2}).*", value)
        if match_re:
            date = '20' + match_re.group(1) + '-' + match_re.group(2) + '-01'
            # date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        else:
            date = datetime.datetime.strptime("1971-1-1", "%Y-%m-%d").date()
        # print(date)

        return date

    def get_goods_name(self, value):
        match_re = re.match("(.*?)\d{4}.*", value)
        if match_re:
            goods_name = match_re.group(1)
        else:
            goods_name = value

        return goods_name
