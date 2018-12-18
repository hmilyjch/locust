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

    @task(4)
    def searchAuthors(self):
        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)
        print('search with author: {} '.format(data['author']) )
        print(data['author'])
        html = self.client.get("/searchAuthors?name=李白")
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








