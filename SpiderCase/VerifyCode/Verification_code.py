"""
日期：2019/4/9
功能：极速验证码识别
准备工作：Chrome浏览器，ChromeDriver，Selenium库
未解决问题：当出现：哇，怪物吃掉了拼图，请3秒后重试时，只能再次重新运行程序；还未添加判断代码
editor:Shirmay1
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from PIL import Image


class CrackGeetest:
    def __init__(self):
        self.url = 'https://www.geetest.com/Sensebot'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)

    def get_button(self):
        """
        选择在线体验》滑动验证》获取初始验证按钮
        :return:验证按钮对象
        """
        #在线体验点击
        button1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gt-sensebot-mobile"]/div[1]/div/div[2]/div/p[3]/a')))
        button1.click()
        time.sleep(2)
        #滑动验证点击
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gt-sensebot-mobile"]/div[2]/section[3]/div/div[2]/div[1]/ul/li[2]')))
        button.click()
        time.sleep(2)
        #验证按钮点击
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="captcha"]/div[3]/div[2]/div[1]/div[3]')))
        return button

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.XPATH, '//canvas[@class="geetest_canvas_slice geetest_absolute"]')))
        time.sleep(2)
        location = img.location
        size = img.size
        left, top, right, bottom = location['x'], location['y'], location['x']+size['width'], location['y']+size['height']
        return left, top, right, bottom

    def get_image(self, name='image.png'):
        """
        获取验证码图片
        :param name: 验证码图片名称
        :return: 图片对象
        """
        left, top, right, bottom = self.get_position()
        print('验证码位置：', left, top, right, bottom)
        # 截图，截取当前屏幕图片
        self.browser.save_screenshot('1' + name)
        picture = Image.open('1' + name)
        # 裁剪屏幕图片，获取验证码图片，注意crop(left,top,right,bottom)四个参数相对于屏幕图片的位置距离
        captcha = picture.crop((left, 380, right, 540))
        captcha.save(name)
        return captcha

    @staticmethod
    def is_pixel_equal(image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 有缺口图片1
        :param image2: 无缺口图片2
        :param x: 位置x
        :param y: 位置y
        :return: 判断同一位置像素是否相同
        """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:返回缺口位置
        """
        left = 60
        print('验证码图片宽度和高度:', image1.size)
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                judge_value = self.is_pixel_equal(image1, image2, i, j)
                if judge_value is False:
                    left = i
                    return left

    @staticmethod
    def get_track(distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹列表
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 7 / 10
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track[:-1]

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def crack(self):
        self.browser.get(self.url)
        # 1、点击滑块验证
        button = self.get_button()
        button.click()
        # 2、获取有缺口的图片image2
        image2 = self.get_image('image2.png')
        # 3、关键步骤：执行js改变css样式，显示背景图（即无缺口的图片）
        self.browser.execute_script('document.querySelectorAll("canvas")[2].style=""')
        time.sleep(1)
        # 4、获取没有缺口的图片image1
        image1 = self.get_image('image1.png')
        # 5、比较获取image1和image2像素点差异，找出缺口位置
        gap = self.get_gap(image1, image2)
        print('缺口位置', gap)
        # 6、滑块原始位置距离图片为6，需减去缺口位移6，
        border = 6
        gap -= border
        # 7、根据缺口位移gap，获取移动轨迹
        track = self.get_track(gap)
        print('滑动轨迹', track)
        # 8、拖动滑块按照移动轨迹拖动
        slider = self.get_slider()
        self.move_to_gap(slider, track)
        # 9、判断是否验证成功，如果出现哇，怪物吃掉了拼图，请3秒后重试，失败后重试
        # success = self.wait.until(EC.text_to_be_present_in_element\
        # ((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        # if success == False:
        #     self.crack()
        # else:
        #     print("验证成功")
        # 10、关闭浏览器
        # self.browser.close()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
