import requests
from bs4 import BeautifulSoup
import re
import threading
import time


# 获取ip
def xiciip(page, list_ip, headers):
    for num_page in range(1, page + 1):
        url = "https://www.xicidaili.com/nn/" + str(num_page)
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'lxml')
            trs = soup.find_all('tr')
            for i in range(1, len(trs)):
                tr = trs[i]
                tds = tr.find_all('td')
                ip = tds[1].text
                port = tds[2].text
                protocl = tds[5].text
                # noinspection PyDictCreation
                dict_ip = {}
                dict_ip[protocl.lower()] = '{}://{}:{}'.format(protocl.lower(), ip, port)
                list_ip.append(dict_ip)
    return list_ip


# 检验ip有效性
def checkip(proxies, headers, usefulip):
    try:
        if list(proxies.keys())[0] == 'http':
            r = requests.get('http://icanhazip.com', headers=headers, proxies=proxies, timeout=2)
            urlip = r.text.strip()
            # print('测试网站ip:', urlip)
            if r.status_code == 200:
                proip = re.findall(r'://(.*?):', str(proxies))[0]
                # print('代理ip', proip)
                if urlip == proip:
                    usefulip.append(proxies)
                    print('测试有效代理ip:', proxies)
                    savedata(str(proxies))
                    return usefulip
        else:
            r = requests.get('https://www.baidu.com/', headers=headers, proxies=proxies, timeout=2)
            if r.status_code == 200:
                print('百度有效代理ip:', proxies)
    except Exception as e:
        print('无效ip:', proxies, e)


def savedata(data):
    with open('ip.txt', 'a') as file:
        file.write(data)


def main():
    list_ip = []
    usefulip = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    listip = xiciip(1, list_ip, headers)
    print('总共ip：', listip, len(listip))
    for proxie in listip:
        t = threading.Thread(target=checkip, args=(proxie, headers, usefulip))
        t.start()
        time.sleep(1)
        t.join()
        # checkip(proxie, headers, usefulip)
    print('有用ip', len(usefulip), usefulip)


if __name__ == '__main__':
    main()
