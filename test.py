import sys
from locust import HttpUser, task, constant

class MainTask(HttpUser):
    wait_time = constant(1)
    uuid = "ff34db23-846c-11ee-89c3-0242ac120002"

    @task
    def get_event_uuid(self):
        response = self.client.get("/events/"+self.uuid)
        print(response.text)

if __name__ == "__main__":
    sys.argv = [sys.argv[0], '-f', sys.argv[0], '--host=http://localhost:8080', '--users=2000', '--spawn-rate=200']
    from locust.main import main
    main()