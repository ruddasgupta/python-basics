'''

To run locust -f performance_testing/locust_quickstart.py

'''

from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/todos")
        self.client.get("/todos/1")
