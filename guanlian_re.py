
import re
from locust import TaskSet, task, HttpLocust
class UserBehavior(TaskSet):
    @staticmethod
    def get_key(j):
        key = re.search(r'"key":"[a-zA-Z0-9]+', j).group()[7:]
        print(key)
        return key
    @task(10)
    def test_login(self):
        html = self.client.get('/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456').text
        key = self.get_key(html)
        print(key)
        self.client.get('/login?key='+key+'&phone=13594347817&passwd=123458')
class WebsiteUser(HttpLocust):
    host = 'https://www.apiopen.top'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000