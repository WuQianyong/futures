#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Time    : 2017/1/9 13:17
# @Author  : wuqianyong
# @File    : simple_log.py
# @Software: PyCharm

"""
日志格式化输出

log: 需要优化，有些地方有问题

"""

import logging
import os
import datetime


def set_log(pathname=None):
    # 创建日志文件夹
    if pathname == None:
        pathname = 'log_file'
    path = os.path.join(os.getcwd(), pathname)
    if os.path.exists(path):
        logging.info('log 目录已存在')
    else:
        os.makedirs(path)
        logging.info('创建log_file 成功')
    # 删除5天以前的日志
    if (os.access(path, os.F_OK)
        or os.path.isdir(path)):
        nowdate_last = datetime.date.today() - datetime.timedelta(days=5)
        del_day = str(nowdate_last).replace("-", "")
        for ss in os.walk(path):
            i = 0

            for aa in ss:
                if i == 2:
                    for bb in aa:
                        file_name = bb
                        ss = bb[bb.find('201'):].replace(".log", "")[:8]
                        # print(ss)
                        if ss < del_day:
                            os.remove(os.path.join(path, file_name))
                            # print('移除文件')
                            # print(ss)
                i += 1
        logging.info("删除 %s 前Log日志文件完毕！" % del_day)


def simple_log(log_dir=None, log_name=None):
    if log_dir == None:
        log_dir = 'log_file'
    path = os.path.join(os.getcwd(), log_dir)
    print(path)
    if os.path.exists(path):
        print('log 目录已存在')
    else:
        os.makedirs(path)
        print('创建log_file 成功')
    # 配置日志信息
    if log_name == None:
        log_name = 'demo.log'
    log_name = os.path.join(log_dir, log_name)
    # 创建一个logger实例
    logger = logging.getLogger()
    logger.setLevel("INFO")  # 设置级别为DEBUG，覆盖掉默认级别WARNING
    # 创建一个handler,用于写入日志文件，handler可以把日志内容写到不同的地方
    # logName = "test.log"
    fh = logging.FileHandler(log_name, "w+", encoding='UTF-8')
    fh.setLevel(logging.INFO)
    # 再创建一个handler，用于输出控制台
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)


    # ch.setLevel(logging.DEBUG)
    # 定义handler的格式输出
    log_format = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)-8s %(message)s')
    fh.setFormatter(log_format)  # setFormatter() selects a Formatter object for this handler to use
    # ch.setFormatter(log_format)


    # 为logger添加handler
    logger.addHandler(fh)
    # logger.addHandler(ch)


    set_log(log_dir)
    return logger

if __name__ == '__main__':
    # logging.info('1')
    # logging.warning('2')
    # logging.error('3')
    # logging.critical('4')
    # a = simple_log()
    #
    #
    # a.debug("this is debug message")  # 不输出
    # a.info("this is info message")  # 输出
    # a.warning("this is warning message")  # 输出
    # a.error("this is warning message")  # 输出
    # a.critical("this is warning message")  # 输出

    logging = simple_log()
    logging.info('haha ')
    logging.error("this is warning message")