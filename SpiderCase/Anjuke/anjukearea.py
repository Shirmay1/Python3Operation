"""
日期：2019/2/20 星期二
作者：王雪梅
功能：anjuke主力面积抓取与统计
"""

import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
import re
import time
import sys


class Geturl:
    def __init__(self, headers, url_list):
        self.headers = headers
        self.url_list = url_list

    def geturl(self):
        r = requests.get(self.url_list[-1], headers=self.headers, timeout=30)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        try:
            next_url = soup.find('div', {'class': 'multi-page'}).find_all('a')[-1]['href']
            if next_url:
                while next_url in self.url_list or next_url[32] == '1':
                    break
                else:
                    self.url_list.append(next_url)
                    self.geturl()
            return self.url_list
        except Exception as err:
            print(err)
            return self.url_list


class Getarea:
    def __init__(self, allurl, headers):
        self.allurl = allurl
        self.headers = headers
        self.area_list = []

    def getonearea(self, url):
        try:
            r = requests.get(url, headers=self.headers, timeout=30)
            r.encoding = r.apparent_encoding
            r.raise_for_status()
        except Exception as err:
            print('请求页面出错', err)
            return "产生异常"
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            ul = soup.find('ul', {'class': 'houselist-mod houselist-mod-new'})
            lis = ul.find_all('li')
            for li in lis:
                div1 = li.find('div', {'class': 'house-details'})
                div2 = div1.find_all('div', {'class': 'details-item'})
                spans = div2[0].find_all('span')
                main_area = spans[1].text
                self.area_list.append(main_area)
        except Exception as err:
            print('解析页面错误', err)
            return ["null"]

    def getarea(self):
        for url in self.allurl:
            self.getonearea(url)
        return self.area_list


class Savaarea:
    def __init__(self, arealist, name):
        self.area_list = arealist
        self.name = name.rstrip()

    # 数据统计
    def countarea(self):
        house_data = []
        area_dict = dict(Counter(self.area_list))
        total_num = 0
        for num in area_dict.values():
            total_num += num
        # 字典；面积数量键值对
        # print(area_dict)
        # house_data = sorted(area_dict.items(),key = lambda item:int(item[0].strip('m²')))
            house_data = sorted(area_dict.items(), key=lambda item: item[1])
        house_data.append(total_num)
        house_data.append(self.name)
        resultdata = tuple(reversed(house_data))
        print(resultdata)
        return resultdata

    # 存入Excel
    def savedata(self):
        resultdata = self.countarea()
        with open('anjukedata.csv', 'a', encoding='utf_8_sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(resultdata)


class Data:
    def __init__(self, cookie, city):
        self.cookie = cookie
        self.city = city

    def mainprocess(self):
        with open('housename', 'r', encoding='UTF_8_sig')as file:
            time_start = time.time()
            num = 1
            headers = {
                'cookie': self.cookie,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36'
            }
            for name in file:
                name1 = re.findall(r'(.*?)@', name)[0]
                id1 = re.findall(r'@(\d+)', name)[0]
                url = 'https://' + self.city + '.anjuke.com/sale/?kw=' + name1 + '&k_comm_id=' + id1
                url_list = [url]
                # 获取单个小区所有页面链接
                my_url = Geturl(headers, url_list)
                allurl = my_url.geturl()
                # 获取单个小区所有面积
                my_area = Getarea(allurl, headers)
                arealist = my_area.getarea()
                # 存入excel
                my_house = Savaarea(arealist, name)
                my_house.savedata()
                time_end = time.time()
                total_time = time_end - time_start
                print('已爬{}个，花费时间{:.2f}秒，{}分钟'.format(num, total_time, int(total_time / 60)))
                num += 1
                print('*******************************************************************')


with open('savecookie', 'r', encoding='UTF_8_sig')as f:
    cookie1 = f.read().rstrip()
city1 = input("请输入安居客城市拼音:")
mydata = Data(cookie1, city1)
mydata.mainprocess()
print("Unexpected error:", sys.exc_info())  # sys.exc_info()返回出错信息
raw = input('press enter key to exit')  # 这儿放一个等待输入是为了不让程序退出
