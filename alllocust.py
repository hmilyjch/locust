from locust import TaskSet, task, HttpLocust
from gevent._semaphore import Semaphore
from locust import events
import json
import queue
import csv

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

events.hatch_complete+=on_hatch_complete


class UserBehavior(TaskSet):
    @staticmethod
    def get_content(j):
        print(j)
        tree = json.loads(j)
        print(tree['result']['content'])
        return tree['result']['content']

    @task(1)
    def EmailSearch(self):
        html = self.client.get("/EmailSearch?number=1012002")
        assert '200' in html, "Response error:" + html

    @task(2)
    def searchMusic(self):
        html = self.client.get("/searchMusic")
        assert '200' in html, "Response error:" + html

    @task(3)
    def musicRankings(self):
        html = self.client.get("/musicRankings")
        assert '200' in html, "Response error:" + html

    @task(4)
    # 使用参数 循环使用auth.csv中参数，并访问"/searchAuthors?name="+data['author']"
    def searchAuthors(self):
        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)
        print('search with author: {} '.format(data['author']) )
        print(data['author'])
        self.locust.user_data_queue.put_nowait(data)
        html = self.client.get("/searchAuthors?name="+data['author']).text
        print(html)
        assert '200' in html, "Response error:" + html


    @task(5)
    def singlePoetry(self):
        html = self.client.get("/singlePoetry").text
        content = self.get_content(html)
        assert '200' in html, "Response error:" + html

        #随机一句古诗词取内容，再模糊搜索古诗词---这里使用关联
        # likePoetry?name=誓将挂冠去，觉道资无穷。
        self.client.get("/likePoetry?name="+content).text
        assert '200' in html, "Response error:" + html

    def on_start(self):
        all_locusts_spawned.wait()

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://api.apiopen.top/"
    user_data_queue = queue.Queue()
    with open('auth.csv', newline='',encoding='UTF-8') as csvfile:  # 此方法:当文件不用时会自动关闭文件
        csvReader = csv.reader(csvfile)
        for content in csvReader:
            data = {
                "author": content[0],
            }
            user_data_queue.put_nowait(data)


    min_wait = 1000
    max_wait = 5000

