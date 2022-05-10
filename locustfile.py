from locust import HttpUser, TaskSet, task


class MyLocust(HttpUser):
    @task(2)
    def basic_load_test(self):
        self.client.get("/")

    @task(1)
    def predict(self):
        self.client.post("/predict")

    min_wait = 1000
    max_wait = 5000
   
    host = "https://udacity-azure-course2.azurewebsites.net"