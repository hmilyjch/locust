from locust import TaskSet, task, HttpLocust
import csv
class UserBehavior(TaskSet):
    def on_start(self):
        self.index = 0
    @task
    def test_visit(self):
        url = self.locust.share_data[self.index]
        print('visit url: %s' % url)
        self.index = (self.index + 1) % len(self.locust.share_data)
        self.client.get(url)
class WebsiteUser(HttpLocust):
    host = 'https://api.apiopen.top'
    task_set = UserBehavior
    # share_data = ['url1', 'url2', 'url3', 'url4', 'url5']
    share_data = []
    with open('CSVtest.csv', newline='') as csvfile:  # 此方法:当文件不用时会自动关闭文件
        csvReader = csv.reader(csvfile)
        for content in csvReader:
            share_data.append(content[1])
    min_wait = 1000
    max_wait = 3000