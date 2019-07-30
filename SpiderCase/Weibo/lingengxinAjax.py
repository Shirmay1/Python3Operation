"""
功能：抓取某明星微博前两页内容
日期：2019/3/27
editor：Shrimay1
知识点：微博属于异步请求，xhr里面查找ajax请求
       requestheadets里面出现这个：X-Requested-With: XMLHttpRequest，代表是Ajax请求
       Ajax，异步的JavaScript和XML，它不是一门编程语言，而是利用JavaScript在保证页面不被刷新、页面链接不改变的情况下
             与服务器交换数据并更新部分网页的技术
"""

from urllib.parse import urlencode
import requests
from pyquery import PyQuery
from pymongo import MongoClient


class Weibolist:
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    headers = {
        'Host': 'm.weibo.cn',
        'Accept': "application/json, text/plain, */*",
        'Referer': "https://m.weibo.cn/u/1730726637",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/74.0.3710.0 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest"
        }
    client = MongoClient()
    db = client.weibo
    collection = db.weibo

    def get_page(self, pagenum):
        params = {
            "type": "uid",
            "value": "1730726637",
            "containerid": "1076031730726637",
            'page': pagenum
        }
        # urlencode()将字典编码为url形式的字符串
        url = self.base_url + urlencode(params)
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                # json()将json格式的字符串转换成字典返回
                return response.json()
        except requests.ConnectionError as err:
            print('Error', err.args)

    @staticmethod
    def parse_page(json):
        if json:
            items = json['data']['cards']
            for item in items:
                try:
                    item = item['mblog']
                    # noinspection PyDictCreation
                    weibo = {}
                    weibo['id'] = item['id']
                    # PyQuery().text()借pyquery将正文中的html标签去掉
                    weibo['text'] = PyQuery(item['text']).text()
                    weibo['attitudes'] = item['attitudes_count']
                    weibo['comments'] = item['comments_count']
                    weibo['reposts'] = item['reposts_count']
                    # 使用了 yield 的函数被称为生成器（generator）
                    # 每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
                    # 并在下一次执行 next() 方法时从当前位置继续运行。
                    yield weibo
                except Exception as err:
                    print('没有mblog这个键：', err)

    def save_to_mongo(self, data):
        # 存储数据到mongodb
        if self.collection.insert_many(data):
            print('Saved to Mongo')


if __name__ == '__main__':
    weibo_list = []
    myweibo = Weibolist()
    for page in range(1, 10):
        text = myweibo.get_page(page)
        results = myweibo.parse_page(text)
        for result in results:
            print(result)
            weibo_list.append(result)
    myweibo.save_to_mongo(weibo_list)
