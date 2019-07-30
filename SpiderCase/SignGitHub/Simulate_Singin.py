'''
日期：2019/4/10
功能：模拟登陆并爬取github
准备工作：requests库，lxml库
editor:Shirmay1
'''
import requests
from lxml import etree
class Login:
    def __init__(self):
        self.headers = {
            'Host': "github.com",
            'Referer': "https://github.com/login?return_to=%2Fjoin",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3710.0 Safari/537.36"
        }
        #登陆url
        self.login_url = 'https://github.com/login'
        #分析后的真实url
        self.post_url = 'https://github.com/session'
        #成功登陆后，要访问的url
        self.logined_url = 'https://github.com/settings/profile'
        # requests库中Session，维持一个会话，自动处理Cookies
        self.session = requests.Session()

    # 获取authenticity_token信息
    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')[0]
        print('authenticity_token：',token)
        return token
        
    #登陆后获取个人名称和邮箱
    def profile(self,html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')
        email= selector.xpath('//select[@id="user_profile_email"]/option[2]/text()')
        print(name,email)
        
    #模拟登陆，实现登陆
    def login(self,Username,password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': Username,
            'password': password
        }
        
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print('登陆成功')
            
        # 登陆后到其他页面https://github.com/settings/profile爬取个人名称和邮箱
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

if __name__ == "__main__":
    login = Login()
    login.login(Username='Shirmay1', password='自己的密码')
