from locust import HttpUser, TaskSet, task


class MyLocust(HttpUser):
    @task(2)
    def basic_load_test(self):
        self.client.get("/")

    @task(1)
    def predict(self):
        data = {"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0}, "PTRATIO": {"0": 15.3}, "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}}
        self.client.post("/predict", json= data)
    min_wait = 1000
    max_wait = 5000
   
    host = "https://udacity-azure-course2.azurewebsites.net"