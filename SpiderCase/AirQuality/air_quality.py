"""
editor: Shirmay1
date:2019/08/11
function:抓取空气质量数据
文章思路链接：https://blog.csdn.net/weixin_43411585/article/details/99202695
"""
import requests
import execjs
import json


# Params
method = 'GETDETAIL'  # method = 'GETCITYWEATHER'
city = '苏州'
type1 = 'HOUR'
start_time = '2019-08-10 00:00:00'
end_time = '2019-08-10 23:00:00'

# Compile javascript
with open('air.js', 'r', encoding='utf8') as file:
    js_text = file.read()
    ctx = execjs.compile(js_text)

# Get params
js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type1, start_time, end_time)
params = ctx.eval(js)

# Get encrypted response text
header = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.aqistudy.cn",
    "Origin": "https://www.aqistudy.cn",
    "Referer": "https://www.aqistudy.cn/html/city_detail.html?v=1.8",
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/75.0.3770.100 Safari/537.36',
    "X-Requested-With": "XMLHttpRequest"}
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params}, headers=header)

# Decode data
js = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js)
data = json.loads(decrypted_data)
data_rows = data['result']['data']['rows']
for row in data_rows:
    print(row)
