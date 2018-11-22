from locust import HttpLocust, TaskSet, task
class WebsiteTasks(TaskSet):
    # def on_start(self):
    #     self.client.post("/login", {
    #     "username": "test",
    #     "password": "123456"
    #     })
    @task(1)
    def wetherApi(self):
        self.client.get("/weatherApi?city=北京")
    @task(2)
    def satinApi(self):
        self.client.get("/satinApi?type=1&page=1")

    @task(3)
    def novelApi(self):
        self.client.get("/novelApi")

    @task(4)
    def femaleNameApi(self):
        self.client.get("/femaleNameApi?page=1")

    @task(5)
    def findStatistics(self):
        self.client.get("/findStatistics?appKey=00d91e8e0cca2b76f515926a36db68f5")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "https://www.apiopen.top"
    min_wait = 1000
    max_wait = 5000