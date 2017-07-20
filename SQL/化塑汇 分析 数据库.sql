/***create database if not exists `hsh_fx`;***/
/*** 创建 大连 日行情表 **/
use `hsh_fx`;
DROP TABLE if EXISTS `t_dalian_dayquotes`;
CREATE TABLE `t_dalian_dayquotes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(50) DEFAULT NULL COMMENT '商品名称',
  `delivery_month` datetime DEFAULT NULL COMMENT '交割月份',
  `open_price` double DEFAULT NULL COMMENT '开盘价',
  `highest_price` double DEFAULT NULL COMMENT '最高价',
  `lowest_price` double DEFAULT NULL COMMENT '最低价',
  `close_price` double DEFAULT NULL COMMENT '收盘价',
  `pre_settlement_price` double DEFAULT NULL COMMENT '前结算价',
  `settlemnt_price` double DEFAULT NULL COMMENT '结算价',
  `change` double DEFAULT NULL COMMENT '涨跌',
  `change_1` double DEFAULT NULL COMMENT '涨跌1',
  `deal_volume` double DEFAULT NULL COMMENT '成交量',
  `position_volume` double DEFAULT NULL COMMENT '持仓量',
  `position_volume_change` double DEFAULT NULL COMMENT '持仓量变化',
  `deal_amount` double DEFAULT NULL COMMENT '成交额',
  `data_date` datetime DEFAULT NULL COMMENT '数据日期',
  `updated` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=232605 DEFAULT CHARSET=utf8;


/**     大连夜盘行情  *****/
use `hsh_fx`;
DROP TABLE if EXISTS `t_dalian_nightquotes`;
CREATE TABLE `t_dalian_nightquotes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(50) DEFAULT NULL COMMENT '商品名称',
  `delivery_month` datetime DEFAULT NULL COMMENT '交割月份',
  `open_price` double DEFAULT NULL COMMENT '开盘价',
  `highest_price` double DEFAULT NULL COMMENT '最高价',
  `lowest_price` double DEFAULT NULL COMMENT '最低价',
  `new_price` double DEFAULT NULL COMMENT '最新价',
  `pre_settlement_price` double DEFAULT NULL COMMENT '前结算价',
  `buy_price` double DEFAULT NULL COMMENT '买价',
  `sell_price` double DEFAULT NULL COMMENT '卖价',
  `change` double DEFAULT NULL COMMENT '涨跌',
  `deal_volume` double DEFAULT NULL COMMENT '成交量',
  `position_volume` double DEFAULT NULL COMMENT '持仓量',
  `position_volume_change` double DEFAULT NULL COMMENT '持仓量变化',
  `deal_amount` double DEFAULT NULL COMMENT '成交额',
  `data_date` datetime DEFAULT NULL COMMENT '数据日期',
  `updated` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61593 DEFAULT CHARSET=utf8;

--- 郑州 日行情

drop TABLE  if EXISTS t_zhengzhou_dayquotes;
CREATE TABLE `t_zhengzhou_dayquotes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(50) DEFAULT NULL COMMENT '商品名称',
  `delivery_month` datetime DEFAULT NULL COMMENT '交割月份',
	`yesterday_settlement_price` double DEFAULT NULL COMMENT '昨结算',
  `open_price` double DEFAULT NULL COMMENT '开盘价',
  `highest_price` double DEFAULT NULL COMMENT '最高价',
  `lowest_price` double DEFAULT NULL COMMENT '最低价',
  `close_price` double DEFAULT NULL COMMENT '收盘价',

  `settlemnt_price` double DEFAULT NULL COMMENT '今结算价',
  `change` double DEFAULT NULL COMMENT '涨跌',
  `change_1` double DEFAULT NULL COMMENT '涨跌1',
  `deal_volume` double DEFAULT NULL COMMENT '成交量',
  `empty_volume` double DEFAULT NULL COMMENT '空盘量',
  `change_volume` double DEFAULT NULL COMMENT '增减量',
  `deal_amount` double DEFAULT NULL COMMENT '成交额',
  `data_date` datetime DEFAULT NULL COMMENT '数据日期',
	`delivery_settlement_price` double DEFAULT NULL COMMENT '交割结算价',
  `updated` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新日期',
  PRIMARY KEY (`id`),
  UNIQUE KEY `data_date` (`data_date`,`goods_name`,`delivery_month`)
) ENGINE=InnoDB AUTO_INCREMENT=232605 DEFAULT CHARSET=utf8;



/***create database if not exists `hsh_fx`;***/
/*** 创建   日行情表 **/
use `hsh_fx`;
drop TABLE  if EXISTS t_dayquotes;
CREATE TABLE `t_dayquotes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(50) DEFAULT NULL COMMENT '商品名称',
  `delivery_month` datetime DEFAULT NULL COMMENT '交割月份',
  `open_price` double DEFAULT NULL COMMENT '开盘价',
  `highest_price` double DEFAULT NULL COMMENT '最高价',
  `lowest_price` double DEFAULT NULL COMMENT '最低价',
  `close_price` double DEFAULT NULL COMMENT '收盘价',
  `pre_settlement_price` double DEFAULT NULL COMMENT '前结算价',
  `settlement_price` double DEFAULT NULL COMMENT '今结算价',
	`deal_volume` double DEFAULT NULL COMMENT '成交量',
  `position_volume` double DEFAULT NULL COMMENT '持仓量',
  `change_1` double DEFAULT NULL COMMENT '涨跌1',
  `change_2` double DEFAULT NULL COMMENT '涨跌2',

  `position_volume_change` double DEFAULT NULL COMMENT '持仓量变化',
  `deal_amount` double DEFAULT NULL COMMENT '成交额',
  `data_date` datetime DEFAULT NULL COMMENT '数据日期',
  `updated` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
