
from locust import TaskSet, task, HttpLocust
import queue
import csv
class UserBehavior(TaskSet):
    @task
    def test_register(self):
        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)
        print('register with user: {}, pwd: {} '.format(data['username'], data['password'])\
              ,data['email'],data['phone'])

        payload = {
             'username': data['username'],
             'password': data['password'],
             'email': data['email'],
             'phone': data['phone']
            }
        self.client.post('/register', data=payload)
        self.locust.user_data_queue.put_nowait(data)

class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    user_data_queue = queue.Queue()

    with open('csvtest2.csv', newline='') as csvfile:  # 此方法:当文件不用时会自动关闭文件
        csvReader = csv.reader(csvfile)
        for content in csvReader:
            data = {
                "username": content[0],
                "password": content[1],
                "email": content[2],
                "phone": content[3],
            }
            user_data_queue.put_nowait(data)



    min_wait = 1000
    max_wait = 3000