#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : phan_demo
# Fatures:
# Author : qianyong
# Time   : 2017-06-01 16:19
# Version: V0.0.1
#
from selenium import webdriver
import time

# profile_dir = r''
# driver = webdriver.Chrome(executable_path=r'C:\Users\wqy\AppData\Local\Google\Chrome\Application\chromedriver.exe')
# driver = webdriver.Firefox(executable_path=r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')
print('开始启动天眼查')
dcap = {"phantomjs.page.settings.userAgent": (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")}
driver = webdriver.PhantomJS(desired_capabilities=dcap)
# driver = webdriver.Firefox(executable_path='D:\\drivers\\geckodriver.exe')

driver.maximize_window()
company_name = '湖州永久电线电缆有限公司'
# 打开天眼查首页

index_url = 'http://www.tianyancha.com/'
driver.get(index_url)
print('打开 {}'.format( driver.title))
if driver.title == 'Error':
    time.sleep(5)
    driver.get(index_url)
    print(driver.title)
time.sleep(5)
driver.find_element_by_id("live-search").send_keys(company_name)
print('天眼查搜索 {}'.format(company_name))
time.sleep(3)
# button = driver.find_element_by_class_name('input-group-addon search_button')
button_s = driver.find_elements_by_tag_name('span')
for b in button_s:
    if b.text == '天眼一下':
        print('点击')
        b.click()
        break


time.sleep(10)
print('打开 {} 的搜索结果'.format(company_name))
# driver.get(index_url)
# time.sleep(5)
# print(driver.title)
#
#
#
#
# search_url = 'http://www.tianyancha.com/search?key={}&checkFrom=searchBox'.format(company_name)
# print(search_url)
# driver.get(search_url)
# time.sleep(30)
# print(driver.title)

# 搜索结果
search_list = driver.find_elements_by_xpath('//*/a[@class="query_name search-new-color ng-isolate-scope"]')

flag = False
for s_item in search_list:
    records = s_item.find_elements_by_tag_name('span')

    search_url = s_item.get_attribute('href')
    search_name = [record.text for record in records][0]
    print('{}  的 链接是 {}'.format(search_name,search_url))

    if search_name == company_name:

        flag = True
        break
print('{}  的 链接是 {}'.format(search_name, search_url))
if not flag:
    print('不存在  搜索的公司:{}'.format(company_name))
else:
    print('存在 搜索的公司:{}'.format(company_name))


    time.sleep(2)
    driver.get(search_url)
    # driver.get("http://www.tianyancha.com/company/23402373")


    print('sleep 30')
    time.sleep(30)
    print(driver.title)


    # 先点击 详情
    try:
        xiang = driver.find_element_by_xpath('//*/a[@ng-show="needFolder"]')
        xiang.click()
        print('已经点击 经营范围 的详细')
        # print(xiang.text)
    except Exception as e:
        # print(e)
        pass

    # 公司的联系信息

    contact_table = driver.find_elements_by_xpath('//*/div[@class="in-block vertical-top"]')
    contact_table2 = driver.find_elements_by_xpath('//*/div[@class="in-block vertical-top overflow-width mr20"]')

    print(len(contact_table))
    info_list = [contact_table, contact_table2]
    for info_table in info_list:
        for contact_item in info_table:

            item_list = contact_item.find_elements_by_tag_name('span')
            if item_list:
                for item in item_list:
                    print('item ----> {}'.format(item.text))

    time.sleep(1)
    # 公司的基本信息1
    base_table1 = driver.find_element_by_xpath('//*/table[@class="table companyInfo-table text-center f14"]')
    base_content_list = base_table1.find_elements_by_tag_name('td')
    for base_content in base_content_list:
        print('base_info ----- > {} '.format(base_content.text.replace('他的所有公司 >', '')))

    # 公司的基本信息2

    base_div = driver.find_element_by_xpath('//*/div[@class="row b-c-white company-content base2017"]')
    base_content_td_name = base_div.find_elements_by_class_name('c8')
    # base_content_td_content = base_div.find_elements_by_class_name('ng-binding')

    for z in base_content_td_name:
        if z.text:
            print(z.text)

driver.quit()
