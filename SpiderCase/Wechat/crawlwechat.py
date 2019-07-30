"""
功能：Appium爬取微信朋友圈：昵称，朋友圈发表时间
日期：2019/4/14
准备工作：安装好Appium,mongodb,Android手机，微信app
注意点：不同的机型，可能查找的元素id不一致，本机是vivoX6D;朋友圈内容暂时没有找到爬取出来
editor:Shirmay1
"""
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from time import sleep
import time
import re


PLATFORM = 'Android'  # 平台
DEVICE_NAME = 'MI_NOTE_Pro'  # 设备名称 通过 adb devices -l 获取
APP_PACKAGE = 'com.tencent.mm'  # APP包名
APP_ACTIVITY = '.ui.LauncherUI'  # 入口类名
DRIVER_SERVER = 'http://localhost:4723/wd/hub'  # Appium地址
# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'moments'
MONGO_COLLECTION = 'moments'
# 滑动间隔
SCROLL_SLEEP_TIME = 1


class Processor:
    @staticmethod
    def date(datetime):
        """
        处理时间
        :param datetime: 原始时间
        :return: 处理后时间
        """
        if re.match('\\d+分钟前', datetime):
            minute = re.match('(\\d+)', datetime).group(1)
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(minute) * 60))
        if re.match('\\d+小时前', datetime):
            hour = re.match('(\\d+)', datetime).group(1)
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(hour) * 60 * 60))
        if re.match('昨天', datetime):
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60))
        if re.match('\\d+天前', datetime):
            day = re.match('(\\d+)', datetime).group(1)
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(day) * 24 * 60 * 60))
        return datetime


class Moments:
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': "True"
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]
        # 处理器
        self.processor = Processor()

    def enter(self):
        """
        进入朋友圈
        :return:
        """
        # 选项卡
        time.sleep(15)
        tab = self.driver.find_elements(By.XPATH, '//*[@resource-id="com.tencent.mm:id/r4"]')[2]
        tab.click()
        time.sleep(10)
        # 朋友圈
        moment = self.driver.find_element(By.ID, 'android:id/title')
        moment.click()
        print("已进入朋友圈")

    def crawl(self):
        """
        爬取
        :return:
        """
        for i in range(15):
            time.sleep(2)
            # 上滑
            self.driver.swipe(300, 1000, 300, 300)
            # 当前页面显示的所有状态
            items = self.driver.find_elements(By.XPATH, '//*[@resource-id="com.tencent.mm:id/ej_"]')
            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element\ 
                    (By.XPATH, '//*[@resource-id="com.tencent.mm:id/b5o"]').get_attribute('text')
                    # # 正文
                    # content = item.find_element \
                    # (By.XPATH, '//*[@resource-id="com.tencent.mm:id/kt"]').get_attribute('text')
                    #
                    # 日期
                    date = item.find_element\ 
                    (By.XPATH, '//*[@resource-id="com.tencent.mm:id/eec"]').get_attribute('text')
                    # 处理日期
                    date = self.processor.date(date)
                    print(nickname, date)
                    data = {
                        'nickname': nickname,
                        # 'content': content,
                        'date': date,
                    }
                    # 插入MongoDB，为了去除重复，这里调用了update_one()方法，
                    # 根据昵称和正文来查询信息，如果信息不存在，则插入数据，否则更新数据。
                    # 这个操作的关键点事第三个参数True,此参数设置为True,可以实现存在即更新。不存在则插入的操作
                    self.collection.update_one({'nickname': nickname}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass

    def main(self):
        """
        入口
        :return:
        """
        # 进入朋友圈
        self.enter()
        # 爬取
        self.crawl()


if __name__ == '__main__':
    moments = Moments()
    moments.main()
