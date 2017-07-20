#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : launch
# Fatures: 爬虫启动
# Author : qianyong
# Time   : 2017-06-21 09:17
# Version: V0.0.1
#

import sys, os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from plugins.simple_log import simple_log
import time

import logging
from scrapy.utils.log import configure_logging

from futures.spiders.Dalian.day_quotes_spider import DayQuotes
from futures.spiders.Dalian.night_quotes_spider import NightQuotes
from futures.spiders.Zhengzhou.zzDayQuotes import ZhengzhouDayQuotes
from futures.spiders.Zhengzhou.zzVariety import ZhengZhouVariety
from futures.spiders.HuaxiCun.HuaxiDayQoutes import HuaXiDayQuotes


def run():
    process = CrawlerProcess()
    process.settings = get_project_settings()

    # ================   修改这块 ======================================
    # process.crawl 是添加爬虫

    process.crawl(DayQuotes)  # 大连日行情
    # process.crawl(NightQuotes)  # 大连夜盘行情   ---- 基本无用
    process.crawl(ZhengzhouDayQuotes)  # 郑州日行情
    # process.crawl(ZhengZhouVariety)  # 郑州 期货品种名称和代码对应   --- 目前无用
    process.crawl(HuaXiDayQuotes)  # 华西村日行情

    # =================================================================
    # 启动 上面的 所有爬虫
    process.start()
if __name__ == '__main__':
    configure_logging(install_root_handler=False)
    logging.basicConfig(

        format='%(asctime)s %(filename)s %(funcName)s %(levelname)-8s %(message)s',
        level=logging.INFO
    )
    log_dir = os.path.join(os.path.abspath('.'), 'logfiles')
    log_name = 'futures_{}.log'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))

    logging = simple_log(log_dir, log_name)
    logging.info(log_dir)
    print(sys.argv)
    run()
