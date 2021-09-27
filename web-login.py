# Author naufalpry@gmail.com
# Load Test https://m.klikdokter.com
# Scope on load test at Klikdokter

import time
from locust import HttpUser, TaskSet, task, between

class SubClassTest(TaskSet):

    @task
    def main_page(self):
        self.client.get('/login')


class MainClassTest(HttpUser):
    tasks = [SubClassTest]
    wait_time = between(5, 10)