#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : get_md5
# Fatures:
# Author : qianyong
# Time   : 2017-05-26 18:26
# Version: V0.0.1
#

import hashlib

# _id= "1ede83004b3b979e3bfe83ae74e434dd"

# src = '{2}{1}{0}'.format('（2016）浙0282民特1725号','赵敏、宁波望通锁业有限公司再审民事裁定书','宁波望通锁业有限公司')
# s = src.encode()
# m2 = hashlib.md5()
# m2.update(s)
# print(m2.hexdigest())

body = {
    "companyName": "句容市科发塑料制品有限公司",
    "publishTime": 1446652800000,
    "lianTime": 1446652800000,
    "caseNumber": "（2015）句刑初字第244号",
    "title": "句容市科发塑料制品有限公司、刘某犯虚开增值税专用发票、用于骗取出口退税、抵扣税款发票罪一审刑事判决书",
    "source": 1
}


def get_md5(content):
    src = '{}'.format(content)
    s = src.encode()
    m2 = hashlib.md5()
    m2.update(s)
    id = m2.hexdigest()

    return id

def get_susong_md5(body):
    """
    body is  a  dict about  susong information
    :param body: 
    :return: 
    """
    src = '{0}{1}{2}{3}'.format(body.get('companyName', ''), body.get('caseNumber', ''), body.get('title', ''),
                                body.get('publishTime', ''))
    s = src.encode()
    m2 = hashlib.md5()
    m2.update(s)
    id = m2.hexdigest()
    body.update({'id': id})
    # print(id)
    # print(body)
    return body



if __name__ == '__main__':
    print(get_md5(body))
    print(get_susong_md5(body))


