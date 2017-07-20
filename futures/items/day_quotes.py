#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : day_quotes
# Fatures: 日行情
# Author : qianyong
# Time   : 2017-06-21 10:04
# Version: V0.0.1
#

"""
日行情 item

大连商品 
说明：
(1) 价格：元/吨
(2) 成交量、持仓量：手（按双边计算）
(3) 成交额：万元（按双边计算）
(4) 涨跌＝收盘价－前结算价
(5) 涨跌1=今结算价-前结算价
(6) 合约系列：具有相同月份标的期货合约的所有期权合约的统称
(7) 隐含波动率：根据期权市场价格，利用期权定价模型计算的标的期货合约价格波动率
"""
from scrapy import Field, Item







class ZhengZhouVarietyItem(Item):
    """
    郑州期货分类
    """
    code = Field()  # 代码
    name = Field()  # 种类名称




class DayQuotesItem(Item):
    """
    日行情数据
    """
    goods_name = Field()  # 商品名称
    delivery_month = Field()  # 交割月份
    open_price = Field()  # 开盘价
    highest_price = Field()  # 最高价
    lowest_price = Field()  # 最低价
    close_price = Field()  # 收盘价
    pre_settlement_price = Field()  # 昨结算价
    settlement_price = Field()  # 今结算价

    deal_volume = Field()  # 总成交量
    position_volume = Field()  # 持仓量
    position_volume_change = Field() # 持仓量变化
    change_1 = Field()  # 涨跌 1
    change_2 = Field()  # 涨跌 2

    deal_amount = Field()  # 交易金额
    quote_date = Field()  # 行情日期