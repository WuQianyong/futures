#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : connect_db
# Fatures:
# Author : qianyong
# Time   : 2017-06-21 15:43
# Version: V0.0.1
#

from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


def _conn(db, only=None):
    """
    链接单个数据库
    :param db:
    :param only:
    :return:
    """
    # print(db)
    engine_str = 'mysql+pymysql://{}:{}@{}/{}?charset={}'.format(db.get('user'),
                                                                 db.get('pwd'),
                                                                 db.get('host'),
                                                                 db.get('db'),
                                                                 db.get('charset'))

    engine = create_engine(engine_str)
    session_factory = sessionmaker(bind=engine, autocommit=False,
                                   autoflush=False)

    if only is None:
        base = automap_base()
        base.prepare(engine, reflect=True)
    else:
        metadata = MetaData()
        metadata.reflect(engine, only=only)
        base = automap_base(metadata=metadata)
        base.prepare()

    # 创建数据会话
    session = scoped_session(session_factory)


    return session, base


def conn_orm(DB, TABLENAME):
    """
    用于连接多个 数据库
    :param DB:
    :param TABLENAME:
    :return:
    """
    session_dict, base_dict = {}, {}
    for key in DB.keys():
        # print()
        session, base = _conn(DB.get(key), TABLENAME.get(key))
        session_dict[key] = session
        base_dict[key] = base
    return session_dict, base_dict


if __name__ == '__main__':
    db = {'host': '115.28.93.101:3306',
          'user': 'zhongtai',
          'pwd': 'CQC$zRp1nMSu94nT',
          'db': 'hsh_zt',
          'charset': 'utf8'}

    session, base = _conn(db, only=['crm_user_title'])
    user = base.classes['crm_user_title']
    a = session.query(user.company_name).filter(user.tax_num == '913101207989180476')
    print(list(a))
