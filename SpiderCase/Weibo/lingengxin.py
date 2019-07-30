"""
日期：2019/4/24
功能：抓取某明星微博详细内容，转发量，赞数，评论数
editor:Shirmay1
知识点：true_url = base_url + urlencode(params1)   # 将字典参数转成url的编码形式
       PyQuery(item['text']).text()    # PyQuery().text()借pyquery将正文中的html标签去掉
       yield weibo   # 生成器，每获得一个数据，就返回一个数据
"""


import requests
from urllib.parse import urlencode
from pyquery import PyQuery
import time
import pymongo


def get_data(base_url, since_id):
    params1 = {
                'uid': '1730726637',
                'luicode': '10000011',
                'lfid': '100103',
                'type': '1',
                'q': '林更新',
                'containerid': '1076031730726637',
                'since_id': since_id

            }
    proxies = {'http': 'https://111.77.197.60:808'}
    headers = {
        'Host': "m.weibo.cn",
        'Connection': "keep-alive",
        'Accept': "application/json, text/plain, */*",
        'MWeibo-Pwa': "1",
        'X-XSRF-TOKEN': "55a49b",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
        'Referer': "https://m.weibo.cn/u/1730726637?uid=1730726637",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cache-Control': "no-cache",
        'cache-control': "no-cache"
        }
    true_url = base_url + urlencode(params1)
    resp = requests.get(true_url, headers=headers, proxies=proxies)
    if resp.status_code == 200:
        htmltext = resp.json()
        return htmltext


# 获取微博内容，日期等
def parse_data(json):
    items = json['data']['cards']
    for item in items:
        try:
            item = item['mblog']
            # noinspection PyDictCreation
            weibo = {}
            weibo['id'] = item['id']
            weibo['date'] = item['created_at']    # 微博创建日期
            if len(weibo['date']) == 5:
                if weibo['date'][-3:] == '小时前':
                    weibo['date'] = time.strftime("%Y-%m-%d", time.localtime())
                else:
                    weibo['date'] = '2019-'+weibo['date']
            # PyQuery().text()借pyquery将正文中的html标签去掉
            weibo['text'] = PyQuery(item['text']).text()   # 微博详细内容
            weibo['reposts_count'] = item['reposts_count']   # 微博转发量
            weibo['comments_count'] = item['comments_count']   # 微博评论量
            yield weibo
        except Exception as err:
            print('没有mblog这个键：', err)


# 获取下一次爬取的接口id参数
def change_api(since_id):
    json = get_data(url, since_id)
    result_data = parse_data(json)
    for result in result_data:
        print(result)
        collection.insert_one(result)
        weibo_list.append(result)
    next_since_id = weibo_list[-1]['id']
    weibo_list.pop()
    return next_since_id


def main(since_id, count):
    next_since_id = change_api(since_id)
    all_since_id.append(next_since_id)
    print('第{}次爬取的起始微博内容id:'.format(count), next_since_id)
    time.sleep(1)


url = 'https://m.weibo.cn/api/container/getIndex?'
weibo_list = []
all_since_id = ['4364678039593341']
client = pymongo.MongoClient(host='localhost', port=27017)
dbweibo = client.dbweibo
collection = dbweibo.weibo

if __name__ == '__main__':
    start_time = time.time()
    i = 2
    while i < 10:
        main(all_since_id[-1], i)
        i += 1
    print(type(weibo_list), weibo_list)
    print('爬取的微博总数:', len(weibo_list))
    end_time = time.time()
    cost_time = end_time - start_time
    print('总共花的时间：', cost_time)
