from lxml import etree
from locust import TaskSet, task, HttpLocust
class UserBehavior(TaskSet):
    @staticmethod
    def get_url(html):
        tree = etree.HTML(html)
        # print(tree.xpath('//a[@uigs-id="footer_disclaimer"]/@href')[0])
        url = tree.xpath('//a[@uigs-id="footer_disclaimer"]/@href')[0][20:]   #取到一个url，并把host去掉
        print(url)
        # print(tree.xpath('//li/a[@id="video"]/@href')[0])   #返回一个连接，再继续访问该链接
        # print(tree.xpath('//li[last()-4]/a/@href'))           #返回倒数第4个li
        # return tree.xpath("//div[@class='btnbox']/input[@name='session']/@value")[0]
        # http://www.cnblogs.com/BigFishFly/p/6380016.html
        return url
    @task(10)
    def test_login(self):
        html = self.client.get('/').text
        # username = 'user@compay.com'
        # password = '123456'
        url = self.get_url(html)
        print(url)
        # payload = {
        #     'username': username,
        #     'password': password,
        #     'session': session
        #     }
        # self.client.post('/login', data=payload)
        self.client.get(url)
class WebsiteUser(HttpLocust):
    host = 'https://www.sogou.com'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000