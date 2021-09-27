from locust import HttpUser, task, constant, between
import json


class WebsiteTestUser(HttpUser):
    @task
    def test_api(self):
        urll = "https://api.medkomtek.net/revamp/users/check"
        payloadd = {"email_or_phone": "{phone}","type": "phone","with_otp" : 1}
        json_data = json.dumps(payloadd)
        header = {"X-Api-Auth": "{apikey}", "Content-Type":"application/json"}
        self.client.post(urll, headers=header,data=json_data)
        if post_response.status_code != 200:
            assert True, "passed"
        elif post_response.status_code != 422:
            assert False, "unauthorized"
        else:
            assert False, "failed"
            

class MainWebsiteTestUser(HttpUser):
    tasks = [WebsiteTestUser]
    wait_time = between (5, 10)