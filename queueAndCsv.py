import queue
import csv
import time

class WebsiteUser():
    host = 'http://debugtalk.com'
    user_data_queue = queue.Queue()

    with open('csvtest2.csv', newline='') as csvfile:  # 此方法:当文件不用时会自动关闭文件
        csvReader = csv.reader(csvfile)
        for content in csvReader:
            data = {
                "username": "test".join(content[1]),
                "password": "pwd".join(content[1]),
                "email": "test@debugtalk.test".join(content[1]),
                "phone": "186".join(content[1]),
            }
            user_data_queue.put_nowait(content)

    while True:
        print(user_data_queue.get())
        time.sleep(2)

