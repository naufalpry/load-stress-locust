from locust import HttpUser, task, constant,  between
import json


class GetArticleDetail(HttpUser):
    @task
    def test_api(self):
        urll = "https://api.medkomtek.net/revamp/articles/detail/{article_id}}"
        header = {"X-Api-Auth": "{apikey}"}
        self.client.get(urll, headers=header)
        if post_response.status_code != 200:
            assert True, "passed"
        elif post_response.status_code != 422:
            assert False, "unauthorized"
        else:
            assert False, "failed"

class GetArticleDetail(HttpUser):
    tasks = [GetArticleDetail]
    wait_time = between(5, 10)