#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : __init__.py
# Fatures:
# Author : qianyong
# Time   : 2017-05-23 13:50
# Version: V0.0.1
def get_delivery_date(delivery_str, data_date):
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
    if data_date[3] == '9' and delivery_str[0] == '9':
        return '{}9-{}-01'.format(data_date[:3], delivery_str[1:])

    elif data_date[3] == '9':
        a = int(data_date[:3]) + 1
        return '{}{}-{}-01'.format(a, delivery_str[0], delivery_str[1:])
    else:
        return '{}{}-{}-01'.format(data_date[:3], delivery_str[0], delivery_str[1:])

if __name__ == '__main__':
    print(get_delivery_date('007','2019-06-26'))