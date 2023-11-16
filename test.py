from locust import HttpUser, task, constant, events
from locust.env import Environment
from locust.runners import LocalRunner

class MainTask(HttpUser):
    wait_time = constant(1)
    uuid = "ff34db23-846c-11ee-89c3-0242ac120002"

    @task
    def get_event_uuid(self):
        response = self.client.get("/events/"+self.uuid)
        print(response.text)

if __name__ == "__main__":
    user_class = MainTask
    environment = Environment(user_classes=[user_class])
    runner = LocalRunner(environment)
    environment.runner = runner
    environment.host = "http://localhost:8080" # 변경 필요
    runner.start(2000, spawn_rate=200)
    runner.greenlet.join()
