# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from futures.items.day_quotes import DayQuotesItem
from futures.items.day_quotes import ZhengZhouVarietyItem
from plugins.connect_db import _conn
import logging
from futures.settings import CONNECT_MYSQL, TABLE_LIST
from sqlalchemy import *


class FuturesPipeline(object):
    def process_item(self, item, spider):
        if self.session and self.base:
            day_quotes = self.base.classes[TABLE_LIST[0]]
            # night_quotes = self.base.classes['t_dalian_nightquotes']
            # zz_day_quotes = self.base.classes['t_zhengzhou_dayquotes']
            # variety = self.base.classes['d_zhengzhou_variety']
            if isinstance(item, DayQuotesItem):
                # print('大连 日行情')
                # logging.info(DayQuotesItem)
                # print(self.session,self.base.classes)

                # 添加一个判断，看看数据是否存在

                result = self.session.query(day_quotes.id).filter(day_quotes.goods_name == item.get('goods_name'),
                                                                  day_quotes.quote_date == item.get('quote_date'),
                                                                  day_quotes.delivery_month == item.get(
                                                                      'delivery_month'))
                result_list = list(result)

                # 修改 数据默认值
                goods_name = item.get('goods_name'),
                delivery_month = item.get('delivery_month'),
                open_price = item.get('open_price'),
                if not open_price:
                    open_price = 0

                highest_price = item.get('highest_price'),
                if not highest_price:
                    highest_price = 0

                lowest_price = item.get('lowest_price'),
                if not lowest_price:
                    lowest_price = 0

                close_price = item.get('close_price'),
                if not close_price:
                    close_price = 0

                pre_settlement_price = item.get('pre_settlement_price'),
                settlement_price = item.get('settlement_price'),

                change_1 = item.get('change_1'),
                if not change_1:
                    change_1 = 0

                change_2 = item.get('change_2'),
                if not change_2:
                    change_2 = 0

                deal_volume = item.get('deal_volume'),
                if not deal_volume:
                    deal_volume = 0

                position_volume = item.get('position_volume'),
                if not position_volume:
                    position_volume = 0

                position_volume_change = item.get('position_volume_change', None),
                if not position_volume_change:
                    position_volume_change = 0

                deal_amount = item.get('deal_amount'),
                if not deal_amount:
                    deal_amount = 0

                quote_date = item.get('quote_date'),

                if result_list.__len__() > 0:

                    if result_list.__len__() > 1:
                        logging.warning('日行情数据 {} {} {} {} 有 {} 条记录'.format(item.get('goods_name'),
                                                                            item.get('quote_date'),
                                                                            item.get('delivery_month'),
                                                                            item.get('close_price'),
                                                                            len(result_list))
                                        )
                    else:
                        logging.info('日行情数据 {} {} {} {} 有 {} 条记录'.format(item.get('goods_name'),
                                                                         item.get('quote_date'),
                                                                         item.get('delivery_month'),
                                                                         item.get('close_price'), len(result_list))
                                     )

                    for id_item in result_list:
                        id = id_item[0]
                        onerecord = day_quotes(id=id,
                                               goods_name=goods_name,
                                               delivery_month=delivery_month,
                                               open_price=open_price,
                                               highest_price=highest_price,
                                               lowest_price=lowest_price,
                                               close_price=close_price,
                                               pre_settlement_price=pre_settlement_price,
                                               settlement_price=settlement_price,
                                               change_1=change_1,
                                               change_2=change_2,
                                               deal_volume=deal_volume,
                                               position_volume=position_volume,
                                               position_volume_change=position_volume_change,
                                               deal_amount=deal_amount,
                                               quote_date=quote_date,
                                               updated=func.now())

                        try:
                            self.session.merge(onerecord)
                            self.session.commit()
                            logging.info('数据更新成功： id: {}   {} {} {} {} '.format(id, item.get('goods_name'),
                                                                                item.get('quote_date'),
                                                                                item.get('delivery_month'),
                                                                                item.get('close_price')))
                        except Exception as e:
                            if 'Duplicate' in str(e):
                                logging.info(
                                    '存储数据 id：{}  {} {} {} {} 失败,原因是 数据库已存在该数据 '.format(id, item.get('goods_name'),
                                                                                       item.get('quote_date'),
                                                                                       item.get('delivery_month'),
                                                                                       item.get('close_price')
                                                                                       ))
                            else:
                                logging.error('存储数据 原因：{}      {}       数据：{}'.format(e, id, item))
                            self.session.rollback()
                            # else:
                            # print(result.__len__())
                else:
                    onerecord = day_quotes(goods_name=goods_name,
                                           delivery_month=delivery_month,
                                           open_price=open_price,
                                           highest_price=highest_price,
                                           lowest_price=lowest_price,
                                           close_price=close_price,
                                           pre_settlement_price=pre_settlement_price,
                                           settlement_price=settlement_price,
                                           change_1=change_1,
                                           change_2=change_2,
                                           deal_volume=deal_volume,
                                           position_volume=position_volume,
                                           position_volume_change=position_volume_change,
                                           deal_amount=deal_amount,
                                           quote_date=quote_date,
                                           updated=func.now())
                    #
                    try:
                        self.session.add(onerecord)
                        self.session.commit()
                        logging.info('日行情数据存储成功：{} {} {} {}'.format(item.get('goods_name'),
                                                                    item.get('quote_date'),
                                                                    item.get('delivery_month'),
                                                                    item.get('close_price')))
                    except Exception as e:
                        if 'Duplicate' in str(e):
                            logging.info('日行情存储数据 {} {} {} {} 失败,原因是 数据库已存在该数据 '.format(item.get('goods_name'),
                                                                                        item.get('quote_date'),
                                                                                        item.get(
                                                                                            'delivery_month'),
                                                                                        item.get('close_price')
                                                                                        ))
                        else:
                            logging.error('日行情 存储数据 失败 原因：{}             数据：{}'.format(e, item))
                        self.session.rollback()

                        # elif isinstance(item, ZhengZhouVarietyItem):
                        #     logging.info('郑州 期货品种')
                        #     result = self.session.query(variety.id).filter(variety.code == item.get('code'),
                        #                                                    variety.name == item.get('name'))
                        #
                        #     result_list = list(result)
                        #     if result_list.__len__() > 0:
                        #         if result_list.__len__() > 1:
                        #             logging.warning('郑州 期货品种数据 {} {}  有 {} 条记录'.format(item.get('name'),
                        #                                                                item.get('code'),
                        #                                                                len(result_list))
                        #                             )
                        #         else:
                        #             logging.info('郑州 期货品种数据 {} {}   有 {} 条记录'.format(item.get('name'),
                        #                                                              item.get('code'),
                        #                                                              len(result_list))
                        #                          )
                        #
                        #         for id_item in result_list:
                        #             id = id_item[0]
                        #             onerecord = variety(id=id,
                        #                                       code=item.get('code'),
                        #                                       name=item.get('name'),
                        #                                       updated=func.now())
                        #
                        #             try:
                        #                 self.session.merge(onerecord)
                        #                 self.session.commit()
                        #                 logging.info('郑州 期货品种数据更新成功： id: {}   {} {}  '.format(id, item.get('code'),
                        #                                                                            item.get('name'),
                        #                                                                            ))
                        #             except Exception as e:
                        #                 if 'Duplicate' in str(e):
                        #                     logging.info(
                        #                         '郑州 期货品种存储数据 id：{}  {}  失败,原因是 数据库已存在该数据 '.format(id, item.get('code'),
                        #                                                                           item.get('name')
                        #                                                                           ))
                        #                 else:
                        #                     logging.error('郑州 期货品种存储数据 原因：{}      {}       数据：{}'.format(e, id, item))
                        #                 self.session.rollback()
                        # else:
                        # print(result.__len__())
                        # else:
                        #     onerecord = variety(name=item.get('name'),
                        #                               code=item.get('code'),
                        #
                        #                               updated=func.now())
                        #     #
                        #     try:
                        #         self.session.add(onerecord)
                        #         self.session.commit()
                        #         logging.info('郑州 期货品种存储成功：{}'.format(item))
                        #     except Exception as e:
                        #         if 'Duplicate' in str(e):
                        #             logging.info('郑州 期货品种存储数据 {} {}  失败,原因是 数据库已存在该数据 '.format(item.get('name'),
                        #                                                                        item.get('code'),
                        #
                        #                                                                        ))
                        #         else:
                        #             logging.error('郑州 期货品种 存储数据 失败 原因：{}             数据：{}'.format(e, item))
                        #         self.session.rollback()

        return item

    def open_spider(self, spider):
        try:
            logging.info('打开管道')
            self.session, self.base = _conn(CONNECT_MYSQL, TABLE_LIST)

            logging.info('连接 MySQL  hsh_fx 成功，参数为：{}'.format(CONNECT_MYSQL))
        except Exception as e:
            logging.critical('连接 MySQL 失败')
            self.session, self.base = None, None
