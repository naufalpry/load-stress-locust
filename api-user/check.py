from locust import HttpUser, task, constant
import json


class WebsiteTestUser(HttpUser):
    @task
    def test_api(self):
        urll = "https://api.medkomtek.net/revamp/users/check"
        payloadd = {"email_or_phone": "6283873452691","type": "phone","with_otp" : 1}
        json_data = json.dumps(payloadd)
        header = {"content-type": "application/json", "X-Api-Auth": "{apikey}"}
        self.client.post(urll, data=json_data, headers=header)
        # self.client.post(path="/revamp/users/check", data=json_data,headers=header)
        if post_response.status_code != 200:
            assert True, "passed"
        elif post_response.status_code != 422:
            assert False, "unauthorized"
        else:
            assert False, "failed"

class MainWebsiteTestUser(HttpUser):
    tasks = [WebsiteTestUser]
    # wait_time = between(5, 10)