from locust import TaskSet, task, HttpLocust
from gevent._semaphore import Semaphore
from locust import events


all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

events.hatch_complete+=on_hatch_complete


class UserBehavior(TaskSet):
    @task(1)
    def profile(self):
        all_locusts_spawned.wait()
        self.client.get("/")

    def on_start(self):
        all_locusts_spawned.wait()

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://debugtalk.com"
    min_wait = 1000
    max_wait = 5000








