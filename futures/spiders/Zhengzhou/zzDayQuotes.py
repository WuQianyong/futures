#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : zzDayQuotes
# Fatures:
# Author : qianyong
# Time   : 2017-06-26 13:50
# Version: V0.0.1
#

from scrapy.spiders import Spider
import datetime, time
from scrapy.http import Request
from scrapy.selector import Selector
import logging
import chardet
from futures.items.day_quotes import DayQuotesItem
# 筛选关键字
FITTER_KEY = ['品种月份','小计','总计']
# 产品关键字字典

Zhengzhou_item = {'ME':'甲醇','MA':'甲醇'}

class ZhengzhouDayQuotes(Spider):
    name = 'zhengzhou_day_quotes'

    def start_requests(self):
        base_url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/{}/{}/FutureDataDaily.htm'

        base_url2 = 'http://www.czce.com.cn/portal/exchange/{}/datadaily/{}.htm'
        date_list = self.get_datelist(8)

        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   'Host': 'www.czce.com.cn',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}

        for date in date_list:

            if date < '2015-10-01':
                url = base_url2.format(date[:4], date.replace('-', ''))

            else:
                url = base_url.format(date[:4], date.replace('-', ''))

            yield Request(url=url,headers=headers,callback=self.parse,meta={'data_date': date})

    def parse(self, response):
        # logging.info(response.url)
        data_date = response.meta.get('data_date','1971-01-01')

        # web_stat = response.text
        # logging.info(web_stat)

        # 去除中文乱码
        encoding = chardet.detect(response.body).get('encoding', 'utf-8')
        # print(encoding)
        if encoding == 'GB2312':
            encoding = 'cp936'
        web_text = str(response.body, encoding=encoding, errors='replace')

        # logging.info(web_text)

        table_list = Selector(text=web_text).xpath('//*/table[@id="senfe"]/tr')
        for row in table_list:
            cell_list = row.xpath('td/text()').extract()
            # logging.info(cell_list)
            if cell_list[0].strip() in FITTER_KEY:
                logging.info('{}  {} 被过滤'.format(data_date,cell_list[0]))
            else:
                if cell_list[0][:-3] in Zhengzhou_item.keys():
                    # logging.info(cell_list)
                    item = DayQuotesItem()

                    good_name = cell_list[0][:-3]
                    delivery_str = cell_list[0][-3:]
                    delivery_date = self.get_delivery_date(delivery_str,data_date)

                    item['goods_name'] = Zhengzhou_item.get(good_name)
                    item['delivery_month'] = delivery_date
                    item['pre_settlement_price'] = cell_list[1].replace(',','')
                    item['open_price'] = cell_list[2].replace(',','')
                    item['highest_price'] = cell_list[3].replace(',','')
                    item['lowest_price'] = cell_list[4].replace(',','')
                    item['close_price'] = cell_list[5].replace(',','')
                    item['settlement_price'] = cell_list[6].replace(',','')
                    item['change_1'] = cell_list[7].replace(',','')
                    item['change_2'] = cell_list[8].replace(',','')
                    item['deal_volume'] = cell_list[9].replace(',','')
                    item['position_volume'] = cell_list[10].replace(',','')
                    item['position_volume_change'] = cell_list[11].replace(',','')
                    item['deal_amount'] = cell_list[12].replace(',','')

                    # dsp = cell_list[13].replace(',','').replace('\xa0','')
                    # if dsp == '':
                    #
                    #     item['delivery_settlement_price'] =None
                    # else:
                    #     item['delivery_settlement_price'] = dsp
                    item['quote_date'] = data_date

                    yield item





        logging.info('{}  {} 解析得到 {} 行'.format(response.url,data_date,len(table_list)))

    def get_datelist(self, day_num):
        """
        获取日期列表

        :param day_num: 
        :return: 
        """
        today = datetime.date.today()
        date_list = [(today - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(day_num)]
        # print(date_list)
        return date_list

    def get_delivery_date(self,delivery_str,data_date):
        """
        将 三位的交割日期转换成 日期形式
        
        example：
        
        In[]:get_delivery_date('707','2017-06-26')
        Out[]:'2017-07-01'
        
        In[]:get_delivery_date('007','2019-06-26')
        Out[]:'2020-07-01'
        
        :param delivery_str: 
        :return: 
        """
        if data_date[3]=='9' and delivery_str[0] == '9':
            return '{}9-{}-01'.format(data_date[:3],delivery_str[1:])

        elif data_date[3]=='9':
            a = int(data_date[:3])+1
            return '{}{}-{}-01'.format(a,delivery_str[0],delivery_str[1:])
        else:
            return '{}{}-{}-01'.format(data_date[:3], delivery_str[0], delivery_str[1:])
