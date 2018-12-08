
import re
from locust import TaskSet, task, HttpLocust
class UserBehavior(TaskSet):
    @task(10)
    def test_login(self):
        html = self.client.get('/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456').text
        assert '200' in  html,"Response error:"+html
        assert '13594347817' in html
        assert '5555555555' in html
        self.client.get('/getTangPoetry?page=1&count=20')
class WebsiteUser(HttpLocust):
    host = 'https://www.apiopen.top'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000